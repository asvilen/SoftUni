function encodeAndDecodeMessages() {
    const mainButtonElements = document.querySelectorAll('#main button');
    const decodeButton = mainButtonElements.item(0);
    const encodeButton = mainButtonElements.item(1);

    decodeButton.addEventListener('click', () => {
        const mainTAElements = document.querySelectorAll('#main textarea');
        const taSend = mainTAElements.item(0).value;
        mainTAElements.item(0).value = ''
        mainTAElements.item(1).value = transformMessage(taSend, 1)

    })

    encodeButton.addEventListener('click', () => {
        const mainTAElements = document.querySelectorAll('#main textarea');
        const taReceive = mainTAElements.item(1).value;
        mainTAElements.item(1).value = transformMessage(taReceive, -1);

    })

    function transformMessage(msg, offset) {
        let encodedMSG = "";
        for (const char of msg) {
            const asciNum = char.charCodeAt(0) + offset
            encodedMSG += String.fromCharCode(asciNum)
        }
        return encodedMSG
    }
}