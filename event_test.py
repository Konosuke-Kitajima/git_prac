import qrcode
print("qrcodeを作成します。")
input_data = input("QRコードにいれるデータを入力してください：")

qr = qrcode.QRCode(
    
)
qr.add_data(input_data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white").convert('L')
save_path = input("保存する名前を決めてください：　")
img.save(save_path + '.png')
img.show()
##コメント1を追加する
<<<<<<< HEAD
##yuki
##yukinosnow
=======
>>>>>>> parent of 9d61d2a (yukino)

