function camera(){    

    Quagga.init({
        inputStream: {
            name: 'Live',
            type: 'LiveStream',
            target: document.querySelector('#app'),//divのID
            constraints: {
                facingMode: 'environment',
            },
        },
        locator: {
            patchSize: 'medium',
            halfSample: true,
        },
        numOfWorkers: 2,
        decoder: {
            readers: ['ean_reader']//isbnを読み取るモード
        },
        locate: true,
    }, (err) => {
        if (!err) {
            Quagga.start();
        }
    })

    let code;

    Quagga.onDetected(success => {
        (code = success.codeResult.code);
        let code_c =code.slice(0,3);
        console.log(code);
        if (code.length == 13 && code_c == 978){
            var gc = document.getElementById("cdata");
            gc.value = code;
            document.forms["gcode"].submit();
        }
    })
}


camera()
