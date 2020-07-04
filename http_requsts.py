import requests
def http_requsts(url,data,header,method='post'):
     if method=='get':
         result=requests.get(url,json=data,headers=header)
     else:
         result=requests.post(url,json=data,headers=header)
     print(result.json())
     return(result.json())
# 请求头
header={"X-Lemonban-Media-Type":"lemonban.v2"}
# 调用函数
 # 注册数据
reg_url="http://120.78.128.25:8766/futureloan/member/register"
reg_data={"mobile_phone":15593335599,"pwd":123456789}
# 登录数据
login_url="http://120.78.128.25:8766/futureloan/member/login"
login_data={"mobile_phone":15593335590,"pwd":123456789}
response=http_requsts(login_url,login_data,header)
# 充值数据
recharge_url="http://120.78.128.25:8766/futureloan/member/recharge"
recharge_data={ "member_id":215651, "amount": 100000.00 }
header_2={"X-Lemonban-Media-Type":"lemonban.v2",'Authorization':'Bearer '+response['data']['token_info']['token']}
# # 提现数据
withdraw_url="http://120.78.128.25:8766/futureloan/member/withdraw"
withdraw_data= {"member_id": 215651, "amount": 88888.00}
# # 更改昵称数据
update_url="http://120.78.128.25:8766/futureloan/member/update"
update_data={ "member_id":215651, "reg_name": "左手"}
http_requsts(reg_url,reg_data,header)
http_requsts(login_url,login_data,header)
http_requsts(recharge_url,recharge_data,header_2)
http_requsts(withdraw_url,withdraw_data,header_2)
# http_requsts(update_url,update_data,header_2)