import webbrowser as web
from bs4 import BeautifulSoup
import io
import sys
from urllib import request
#显示系统名称
print("         气象报文查询系统")
print("          数据源：VATPRC")
a=str(input("请输入机场四字码："))
print("正在查询，请等待......")
b=str("https://metar.vatsim.net/metar.php?id=")
c=b+a
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')		#改变标准输出的默认编码
if __name__ == "__main__":
	response = request.urlopen(c)
	html = response.read()
	html = html.decode('utf-8')		#根据网页的编码方式进行解码
	print(html)
	ddd="-----------------------------------------------------------------------------------------------------------------------------------------------------"
	print(ddd[:len(html)])
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')   #改变标准输出的默认编码改回去
f=str(input("输入任意值关闭程序："))