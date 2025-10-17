from flask import Flask,render_template,request,jsonify
import pandas as pd
import math

app=Flask('index.html',template_folder='temp')

@app.route('/')
def index():
   #db 불러오기
   db=pd.read_csv('data/통합공공데이터.csv')
   db.rename(columns={'Unnamed: 0':'번호'},inplace=True)
   page=int(request.args.get('page',1))
   db['번호']=range(1,len(db)+1)

   #페이지 처리
   page=int(request.args.get('page',1))
   per_page=20
   total_pages=math.ceil(len(db)/per_page)
   start=(page-1)*per_page
   end=start+per_page
   db_page=db.iloc[start:end]
   table_db=db_page.to_html(classes="table table-bordered table-hover text-center",index=False)
   return render_template('index.html',
                          title='대체 공공정보사이트',
                          PageName='home.html',
                          table=table_db,
                          total_pages=total_pages,
                          page=page,
                         )


@app.route('/search')
def search():
   keyword = request.args['keyword'].strip()
   page=int(request.args.get('page',1))
      #db 불러오기
   db=pd.read_csv('data/통합공공데이터.csv')
   db.rename(columns={'Unnamed: 0':'번호'},inplace=True)
   db['번호']=range(1,len(db)+1)
   db['url']=db['url'].apply(lambda x:f'<a href="{x}" target="_blank">{x}</a>, rel="noopener noreferrer"')
  
  #필터링
   if keyword:
         filt=(db['기관제공목록명'].str.contains(keyword,case=False,na=False)) | (db['정부24제공목록명'].str.contains(keyword))
         db=db[filt]
 

   #페이지 이동(필터링 이후)
   per_page=20
   total_pages=math.ceil(len(db)/per_page)
   start=(page-1)*per_page
   end=start+per_page
   db_page=db.iloc[start:end]

   table_db=db_page.to_html(classes="table table-bordered table-hover text-center",index=False,escape=False)
   return jsonify({
       'table':table_db,
       'page':page,
       'total_pages':total_pages
   })

if __name__=='__main__':
    app.run(port=5000,debug=True)