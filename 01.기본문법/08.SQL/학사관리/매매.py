
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import json
import time

class CryptoTradingAnalyzer:
    def __init__(self, symbol='bitcoin'):
        self.symbol = symbol
        self.df = None
        self.signals = []
        
    def fetch_price_data(self, days=365):
        """CoinGecko API를 사용하여 가격 데이터 수집"""
        try:
            url = f"https://api.coingecko.com/api/v3/coins/{self.symbol}/market_chart"
            params = {
                'vs_currency': 'usd',
                'days': days,
                'interval': 'daily'
            }
            
            response = requests.get(url, params=params)
            data = response.json()
            
            # 데이터 정리
            prices = data['prices']
            volumes = data['total_volumes']
            
            df = pd.DataFrame(prices, columns=['timestamp', 'price'])
            df['volume'] = [vol[1] for vol in volumes]
            df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('date', inplace=True)
            df.drop('timestamp', axis=1, inplace=True)
            
            self.df = df
            print(f"{self.symbol} 데이터 수집 완료: {len(df)}일치 데이터")
            return True
            
        except Exception as e:
            print(f"데이터 수집 오류: {e}")
            return False
    
    def calculate_technical_indicators(self):
        """기술적 지표 계산"""
        if self.df is None:
            print("먼저 데이터를 수집해주세요.")
            return
        
        df = self.df.copy()
        
        # 이동평균선 (Moving Average)
        df['MA7'] = df['price'].rolling(window=7).mean()
        df['MA21'] = df['price'].rolling(window=21).mean()
        df['MA50'] = df['price'].rolling(window=50).mean()
        
        # RSI (Relative Strength Index)
        delta = df['price'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['RSI'] = 100 - (100 / (1 + rs))
        
        # MACD (Moving Average Convergence Divergence)
        exp1 = df['price'].ewm(span=12).mean()
        exp2 = df['price'].ewm(span=26).mean()
        df['MACD'] = exp1 - exp2
        df['MACD_signal'] = df['MACD'].ewm(span=9).mean()
        
        # 볼린저 밴드 (Bollinger Bands)
        df['BB_middle'] = df['price'].rolling(window=20).mean()
        df['BB_std'] = df['price'].rolling(window=20).std()
        df['BB_upper'] = df['BB_middle'] + (df['BB_std'] * 2)
        df['BB_lower'] = df['BB_middle'] - (df['BB_std'] * 2)
        
        # 변동률
        df['price_change_pct'] = df['price'].pct_change() * 100
        df['volatility'] = df['price_change_pct'].rolling(window=7).std()
        
        self.df = df
        print("기술적 지표 계산 완료")
    
    def generate_trading_signals(self):
        """매매 신호 생성"""
        if self.df is None:
            print("먼저 데이터를 분석해주세요.")
            return
        
        df = self.df.copy()
        signals = []
        
        for i in range(1, len(df)):
            current = df.iloc[i]
            previous = df.iloc[i-1]
            
            signal_type = 'HOLD'
            reasons = []
            confidence = 0
            
            # 매수 신호 조건들
            buy_conditions = 0
            sell_conditions = 0
            
            # 1. 이동평균선 분석
            if current['price'] > current['MA7'] and current['MA7'] > current['MA21']:
                buy_conditions += 1
                reasons.append("단기 상승추세")
            elif current['price'] < current['MA7'] and current['MA7'] < current['MA21']:
                sell_conditions += 1
                reasons.append("단기 하락추세")
            
            # 2. RSI 분석
            if current['RSI'] < 30:  # 과매도
                buy_conditions += 1
                reasons.append("RSI 과매도")
            elif current['RSI'] > 70:  # 과매수
                sell_conditions += 1
                reasons.append("RSI 과매수")
            
            # 3. MACD 분석
            if current['MACD'] > current['MACD_signal'] and previous['MACD'] <= previous['MACD_signal']:
                buy_conditions += 1
                reasons.append("MACD 골든크로스")
            elif current['MACD'] < current['MACD_signal'] and previous['MACD'] >= previous['MACD_signal']:
                sell_conditions += 1
                reasons.append("MACD 데드크로스")
            
            # 4. 볼린저 밴드 분석
            if current['price'] < current['BB_lower']:
                buy_conditions += 1
                reasons.append("볼린저밴드 하단 터치")
            elif current['price'] > current['BB_upper']:
                sell_conditions += 1
                reasons.append("볼린저밴드 상단 터치")
            
            # 5. 거래량 분석
            volume_avg = df['volume'].rolling(window=7).mean().iloc[i]
            if current['volume'] > volume_avg * 1.5:
                if buy_conditions > sell_conditions:
                    buy_conditions += 1
                    reasons.append("거래량 급증")
            
            # 신호 결정
            if buy_conditions >= 3:
                signal_type = 'BUY'
                confidence = min(buy_conditions * 20, 100)
            elif sell_conditions >= 3:
                signal_type = 'SELL'
                confidence = min(sell_conditions * 20, 100)
            elif buy_conditions > sell_conditions and buy_conditions >= 2:
                signal_type = 'WEAK_BUY'
                confidence = 50
            elif sell_conditions > buy_conditions and sell_conditions >= 2:
                signal_type = 'WEAK_SELL'
                confidence = 50
            
            signals.append({
                'date': current.name,
                'price': current['price'],
                'signal': signal_type,
                'confidence': confidence,
                'reasons': ', '.join(reasons) if reasons else '신호 없음',
                'rsi': current['RSI'],
                'macd': current['MACD'],
                'volume': current['volume']
            })
        
        self.signals = signals
        print(f"매매 신호 생성 완료: {len(signals)}개 신호")
    
    def backtest_strategy(self, initial_capital=10000):
        """백테스팅 수행"""
        if not self.signals:
            print("먼저 매매 신호를 생성해주세요.")
            return
        
        capital = initial_capital
        holdings = 0
        trades = []
        portfolio_value = []
        
        for signal in self.signals:
            current_price = signal['price']
            
            if signal['signal'] == 'BUY' and capital > current_price:
                # 매수
                shares_to_buy = capital * 0.8 / current_price  # 80% 투자
                holdings += shares_to_buy
                capital -= shares_to_buy * current_price
                
                trades.append({
                    'date': signal['date'],
                    'type': 'BUY',
                    'price': current_price,
                    'shares': shares_to_buy,
                    'capital': capital
                })
                
            elif signal['signal'] == 'SELL' and holdings > 0:
                # 매도
                capital += holdings * current_price
                trades.append({
                    'date': signal['date'],
                    'type': 'SELL',
                    'price': current_price,
                    'shares': holdings,
                    'capital': capital
                })
                holdings = 0
            
            # 포트폴리오 가치 계산
            total_value = capital + (holdings * current_price)
            portfolio_value.append({
                'date': signal['date'],
                'value': total_value,
                'price': current_price
            })
        
        # 결과 분석
        if portfolio_value:
            final_value = portfolio_value[-1]['value']
            total_return = ((final_value - initial_capital) / initial_capital) * 100
            
            # 벤치마크 대비 성과 (단순 보유)
            initial_price = self.signals[0]['price']
            final_price = self.signals[-1]['price']
            benchmark_return = ((final_price - initial_price) / initial_price) * 100
            
            print(f"\n=== 백테스팅 결과 ===")
            print(f"초기 자본: ${initial_capital:,.2f}")
            print(f"최종 자본: ${final_value:,.2f}")
            print(f"총 수익률: {total_return:.2f}%")
            print(f"벤치마크 수익률: {benchmark_return:.2f}%")
            print(f"알파: {total_return - benchmark_return:.2f}%")
            print(f"총 거래 횟수: {len(trades)}")
            
            return {
                'trades': trades,
                'portfolio_value': portfolio_value,
                'total_return': total_return,
                'benchmark_return': benchmark_return
            }
    
    def analyze_recent_signals(self, days=30):
        """최근 N일간의 신호 분석"""
        if not self.signals:
            print("먼저 매매 신호를 생성해주세요.")
            return
        
        recent_signals = [s for s in self.signals[-days:]]
        
        print(f"\n=== 최근 {days}일간 매매 신호 분석 ===")
        
        for signal in recent_signals[-10:]:  # 최근 10일만 출력
            date_str = signal['date'].strftime('%Y-%m-%d')
            signal_emoji = {
                'BUY': '🟢 매수',
                'SELL': '🔴 매도',
                'WEAK_BUY': '🟡 약매수',
                'WEAK_SELL': '🟠 약매도',
                'HOLD': '⚪ 보유'
            }
            
            print(f"{date_str}: {signal_emoji.get(signal['signal'], signal['signal'])} "
                  f"(신뢰도: {signal['confidence']}%) - ${signal['price']:,.2f}")
            print(f"  └ 사유: {signal['reasons']}")
        
        # 신호 통계
        signal_counts = {}
        for signal in recent_signals:
            signal_type = signal['signal']
            signal_counts[signal_type] = signal_counts.get(signal_type, 0) + 1
        
        print(f"\n신호 분포:")
        for signal_type, count in signal_counts.items():
            print(f"  {signal_type}: {count}회")
    
    def visualize_analysis(self):
        """분석 결과 시각화"""
        if self.df is None:
            print("먼저 데이터를 분석해주세요.")
            return
        
        fig, axes = plt.subplots(3, 1, figsize=(15, 12))
        
        # 1. 가격 및 이동평균선
        axes[0].plot(self.df.index, self.df['price'], label='Price', linewidth=2)
        axes[0].plot(self.df.index, self.df['MA7'], label='MA7', alpha=0.7)
        axes[0].plot(self.df.index, self.df['MA21'], label='MA21', alpha=0.7)
        axes[0].plot(self.df.index, self.df['MA50'], label='MA50', alpha=0.7)
        
        # 매매 신호 표시
        if self.signals:
            buy_signals = [s for s in self.signals if s['signal'] in ['BUY', 'WEAK_BUY']]
            sell_signals = [s for s in self.signals if s['signal'] in ['SELL', 'WEAK_SELL']]
            
            if buy_signals:
                buy_dates = [s['date'] for s in buy_signals]
                buy_prices = [s['price'] for s in buy_signals]
                axes[0].scatter(buy_dates, buy_prices, color='green', marker='^', s=100, label='Buy Signal')
            
            if sell_signals:
                sell_dates = [s['date'] for s in sell_signals]
                sell_prices = [s['price'] for s in sell_signals]
                axes[0].scatter(sell_dates, sell_prices, color='red', marker='v', s=100, label='Sell Signal')
        
        axes[0].set_title(f'{self.symbol.upper()} Price Analysis')
        axes[0].set_ylabel('Price (USD)')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # 2. RSI
        axes[1].plot(self.df.index, self.df['RSI'], label='RSI', color='purple')
        axes[1].axhline(y=70, color='r', linestyle='--', alpha=0.7, label='Overbought (70)')
        axes[1].axhline(y=30, color='g', linestyle='--', alpha=0.7, label='Oversold (30)')
        axes[1].set_title('RSI (Relative Strength Index)')
        axes[1].set_ylabel('RSI')
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)
        
        # 3. MACD
        axes[2].plot(self.df.index, self.df['MACD'], label='MACD', color='blue')
        axes[2].plot(self.df.index, self.df['MACD_signal'], label='Signal', color='red')
        axes[2].bar(self.df.index, self.df['MACD'] - self.df['MACD_signal'], 
                   label='Histogram', alpha=0.3, color='gray')
        axes[2].set_title('MACD')
        axes[2].set_ylabel('MACD')
        axes[2].set_xlabel('Date')
        axes[2].legend()
        axes[2].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()

def main():
    """메인 실행 함수"""
    print("=== 암호화폐 자동매매 분석 프로그램 ===\n")
    
    # 분석할 코인 선택 (CoinGecko ID 형식)
    available_coins = {
        '1': 'bitcoin',
        '2': 'ethereum',
        '3': 'binancecoin',
        '4': 'cardano',
        '5': 'solana'
    }
    
    print("분석할 암호화폐를 선택하세요:")
    for key, coin in available_coins.items():
        print(f"{key}: {coin.upper()}")
    
    choice = input("\n번호를 입력하세요 (기본값: 1): ").strip()
    if not choice:
        choice = '1'
    
    selected_coin = available_coins.get(choice, 'bitcoin')
    print(f"\n{selected_coin.upper()} 분석을 시작합니다...\n")
    
    # 분석 실행
    analyzer = CryptoTradingAnalyzer(selected_coin)
    
    # 1. 데이터 수집
    if not analyzer.fetch_price_data(365):
        print("데이터 수집에 실패했습니다.")
        return
    
    # 2. 기술적 지표 계산
    analyzer.calculate_technical_indicators()
    
    # 3. 매매 신호 생성
    analyzer.generate_trading_signals()
    
    # 4. 최근 신호 분석
    analyzer.analyze_recent_signals(30)
    
    # 5. 백테스팅
    backtest_result = analyzer.backtest_strategy(10000)
    
    # 6. 현재 추천
    latest_signal = analyzer.signals[-1] if analyzer.signals else None
    if latest_signal:
        print(f"\n=== 현재 추천 ===")
        print(f"현재 가격: ${latest_signal['price']:,.2f}")
        print(f"신호: {latest_signal['signal']}")
        print(f"신뢰도: {latest_signal['confidence']}%")
        print(f"근거: {latest_signal['reasons']}")
        
        # 리스크 경고
        print(f"\n⚠️ 투자 주의사항:")
        print(f"- 이 프로그램은 교육/분석 목적입니다")
        print(f"- 실제 투자 시 손실이 발생할 수 있습니다")
        print(f"- 충분한 리서치 후 신중하게 결정하세요")
    
    # 7. 차트 표시 여부 선택
    show_chart = input("\n차트를 표시하시겠습니까? (y/n): ").lower()
    if show_chart == 'y':
        analyzer.visualize_analysis()

if __name__ == "__main__":
    main()