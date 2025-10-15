    // 유효성 검사(공통으로)
    $("[name='hour']").on("input", function() {
        let value = $(this).val();
        // 숫자와 소수점만 허용
        value = value.replace(/[^0-9.]/g, '');
        // 소수점이 여러 개 들어오면 첫 번째만 유지
        value = value.replace(/(\..*?)\..*/g, '$1');
        $(this).val(value);
    });