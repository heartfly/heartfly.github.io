Title: APNS证书生成
Date: 2013-11-24 12:06
Category: iOS
tags: APNS, 推送, PUSH, 证书
Slug: apns-cert-generagion
Author: haxx
Summary: APNS证书生成

* 以下步骤需在App ID产生以后进行:

>1. 登录到 [iPhone Developer Connection Portal](http://developer.apple.com/iphone/manage/overview/index.action) 并点击*App IDs*

>2. 选择对应*App ID*。（开发与发布不一样的。需注意）

>3. 点击App ID旁的*Configure*，然后按下按钮生产 推送通知许可证。根据*向导*的步骤生成一个签名并上传，最后下载生成的许可证。

>4. 通过双击*.cer*文件将你的*aps_developer_identity.cer*引入*Keychain*中。

>6. 打开*Keychain*,在登录证书(*Certificates*)下找到*Apple Development Push Services*项，右键*Apple Development Push Services*，导出*p12*文件，保存为*apns-dev-cert.p12*文件。

>7. 单击展开*Apple Development Push Services* 对*Private Key*做同样操作，保存为*apns-dev-key.p12*文件。

>8. 需要通过终端命令将这些文件转换为*PEM*格式：

    openssl pkcs12 -clcerts -nokeys -out apns-dev-cert.pem -in apns-dev-cert.p12
    openssl pkcs12 -nocerts -out apns-dev-key.pem -in apns-dev-key.p12


>9. 如果你想要移除密码，要么在导出/转换时不要设定或者执行：

    openssl rsa -in apns-dev-key.pem -out apns-dev-key-noenc.pem

>10. 最后，你需要将键和许可文件合成为*apns-dev.pem*文件，此文件在连接到*APNS*时需要使用：

    cat apns-dev-cert.pem apns-dev-key-noenc.pem > apns-dev.pem

