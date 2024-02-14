import qrcode

qrText = input("Enter link, name, or text: ")
fileName = input("File name: ")
frontColor = input("Enter front color: ")
backColor = input("Enter back color: ")

qr = qrcode.QRCode(
version=1,
error_correction=qrcode.constants.ERROR_CORRECT_L,
box_size=20,
border=4,
)

qr.add_data(qrText)
qr.make(fit=True)

qrCodeImage = qr.make_image(fill_color=frontColor, back_color=backColor)
qrCodeImage.save("{}.png".format(fileName))
