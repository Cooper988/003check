【2022.7.22】 更新了签到脚本

## 简介

首次输入邀请码注册免费获得3天，绑定教育邮箱获得360天，每天签到获得1天。本文教大家如何通过脚本自动签到，并自动推送结果到微信上。每步都配了截图，小白也能做。

## 注册GLaDOS

注册地址：
在 https://github.com/glados-network/GLaDOS 实时更新

邀请码:
`LC4CI-CBO6S-RXV13-LT7ND`
免费获得3天
如果你有教育邮箱，可以拉到页面底部申请教育计划**免费获得360天时长**
![在这里插入图片描述](https://picture-1308610694.cos.ap-nanjing.myqcloud.com/202207221453536.png)

## Fork项目到自己的仓库

1. 打开 https://github.com/sicilly/glados-checkin-1
2. 在页面右上角点击Star、Fork
   ![在这里插入图片描述](https://picture-1308610694.cos.ap-nanjing.myqcloud.com/202207221453495.png)

## 配置账户信息

1. 添加action cecrets
   如图所示点击settings-secrets-new repository secret
   ![在这里插入图片描述](https://picture-1308610694.cos.ap-nanjing.myqcloud.com/202207221453647.png)
2. 添加自己账户的信息
   ![在这里插入图片描述](https://picture-1308610694.cos.ap-nanjing.myqcloud.com/202207221453518.png)

如果你只需要签到，不需要微信推送，就只添加一个东西：

| Name   | Value                          |
| ------ | ------------------------------ |
| COOKIE | 你自己的cookie（下一步会说明） |

如果需要微信推送就添加两个东西：

| Name   | Value                           |
| ------ | ------------------------------- |
| COOKIE | 你自己的cookie（下一步会说明）  |
| SCKEY  | 你自己的sendkey（下一步会说明） |

接下来会详细介绍如何获取`COOKIE`和`SCKEY`

### 3. 获取COOKIE

登录glados，按键盘上的`F12`打开开发者工具
进入我的账户，刷新页面
如图所示找到cookie，把 **cookie：** 后面的几行都复制下来，填入上一步对应的value中
![在这里插入图片描述](https://picture-1308610694.cos.ap-nanjing.myqcloud.com/202207221453757.png)

### 3. 获取SCKEY

**（2022.3.23更新：server酱的网站更新了，之前叫SCKEY，现在叫SENDKEY，但是不影响我们后面的操作）**

这是在server酱中获取的，用于绑定微信，给你推送签到后的结果
server酱地址：https://sct.ftqq.com/login
（1）微信扫码登录
![在这里插入图片描述](https://picture-1308610694.cos.ap-nanjing.myqcloud.com/202207221453663.png)
（2）复制SENDKEY
![在这里插入图片描述](https://picture-1308610694.cos.ap-nanjing.myqcloud.com/202207221453170.png)
注意：把刚才复制好的SENDKEY粘贴到下图的Value处，Name就是写SCKEY，不用改！
![在这里插入图片描述](https://picture-1308610694.cos.ap-nanjing.myqcloud.com/202207221453230.png)

两个secret添加好后，就应该是这个样子：
![在这里插入图片描述](https://picture-1308610694.cos.ap-nanjing.myqcloud.com/202207221453368.png)

## 开启Action

![在这里插入图片描述](https://picture-1308610694.cos.ap-nanjing.myqcloud.com/202207221453293.png)
先点击左侧的glados-checkin，然后右边点击Enable workflow
![在这里插入图片描述](https://picture-1308610694.cos.ap-nanjing.myqcloud.com/202207221453331.png)

## 测试运行

此时已经开启了action，为了知道脚本是否能成功运行，我们需要先手动测试一下，点击run workflow
![在这里插入图片描述](https://picture-1308610694.cos.ap-nanjing.myqcloud.com/202207221453339.png)
刷新一下页面发现这个黄点，表示脚本正在运行了，稍等一分钟
![在这里插入图片描述](https://picture-1308610694.cos.ap-nanjing.myqcloud.com/202207221453568.png)
当这个黄点变成绿勾时就是执行完成了
![在这里插入图片描述](https://picture-1308610694.cos.ap-nanjing.myqcloud.com/202207221453814.png)

打开微信看是否收到Server酱发来的通知：

![在这里插入图片描述](https://picture-1308610694.cos.ap-nanjing.myqcloud.com/202207221453852.png)

点进去会看到详细的签到结果，注意并不是每次签到都一定会增加1天，有可能提示你明天再来

这不是脚本的问题，是glados官网设定的有一定几率签到获得天数
![在这里插入图片描述](https://picture-1308610694.cos.ap-nanjing.myqcloud.com/202207221453890.png)

自此就成功了，可以不用管它了，每天大约0点左右都会自动签到

(自动签到的时间写在checkin.yml的cron表达式里，有需要可自行修改)

