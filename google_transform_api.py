import requests
import json
from bs4 import BeautifulSoup
import execjs #必须，需要先用pip 安装，用来执行js脚本
class Py4Js():
  def __init__(self):
    self.ctx = execjs.compile(""" 
    function TL(a) { 
    var k = ""; 
    var b = 406644; 
    var b1 = 3293161072;       
    var jd = "."; 
    var $b = "+-a^+6"; 
    var Zb = "+-3^+b+-f";    
    for (var e = [], f = 0, g = 0; g < a.length; g++) { 
        var m = a.charCodeAt(g); 
        128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023), 
        e[f++] = m >> 18 | 240, 
        e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224, 
        e[f++] = m >> 6 & 63 | 128), 
        e[f++] = m & 63 | 128) 
    } 
    a = b; 
    for (f = 0; f < e.length; f++) a += e[f], 
    a = RL(a, $b); 
    a = RL(a, Zb); 
    a ^= b1 || 0; 
    0 > a && (a = (a & 2147483647) + 2147483648); 
    a %= 1E6; 
    return a.toString() + jd + (a ^ b) 
  };      
  function RL(a, b) { 
    var t = "a"; 
    var Yb = "+"; 
    for (var c = 0; c < b.length - 2; c += 3) { 
        var d = b.charAt(c + 2), 
        d = d >= t ? d.charCodeAt(0) - 87 : Number(d), 
        d = b.charAt(c + 1) == Yb ? a >>> d: a << d; 
        a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d 
    } 
    return a 
  } 
 """)
  def getTk(self,text):
      return self.ctx.call("TL",text)
def buildUrl(text,tk):
  baseUrl='https://translate.google.cn/translate_a/single'
  baseUrl+='?client=t&'
  baseUrl+='s1=auto&'
  baseUrl+='t1=zh-CN&' # zh-CN
  baseUrl+='h1=zh-CN&'
  baseUrl+='dt=at&'
  baseUrl+='dt=bd&'
  baseUrl+='dt=ex&'
  baseUrl+='dt=ld&'
  baseUrl+='dt=md&'
  baseUrl+='dt=qca&'
  baseUrl+='dt=rw&'
  baseUrl+='dt=rm&'
  baseUrl+='dt=ss&'
  baseUrl+='dt=t&'
  baseUrl+='ie=UTF-8&'
  baseUrl+='oe=UTF-8&'
  baseUrl+='otf=1&'
  baseUrl+='pc=1&'
  baseUrl+='ssel=0&'
  baseUrl+='tsel=0&'
  baseUrl+='kc=2&'
  baseUrl+='tk='+str(tk)+'&'
  baseUrl+='q='+text
  return baseUrl
def translate(text):
  header={
    'authority':'translate.google.cn',
    'method':'GET',
    'path':'',
    'scheme':'https',
    'accept':'*/*',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.9', #zh-CN
    'cookie':'',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
'x-client-data':'CIa2yQEIpbbJAQjBtskBCPqcygEIqZ3KAQioo8oBGJGjygE='
  }
  url=buildUrl(text,js.getTk(text))
  res=''
  try:
      r=requests.get(url)
      result=json.loads(r.text)
      if result[7]!=None:
      # 如果我们文本输错，提示你是不是要找xxx的话，那么重新把xxx正确的翻译之后返回
          try:
              correctText=result[7][0].replace('<b><i>',' ').replace('</i></b>','')
              print(correctText)
              correctUrl=buildUrl(correctText,js.getTk(correctText))
              correctR=requests.get(correctUrl)
              newResult=json.loads(correctR.text)
              res=newResult[0][0][0]
          except Exception as e:
              print(e)
              res=result[0][0][0]
      else:
          res=result[0][0][0]
  except Exception as e:
      res=''
      print(url)
      print("翻译"+text+"失败")
      print("错误信息:")
      print(e)
  finally:
      return res
if __name__ == '__main__':
  js=Py4Js()
  a = "Paraphrase generation is an important problem in NLP"
  b = "Paraphrase generation is an important problem in NLP, especially in question answering, information retrieval, information extraction, conversation systems, to name a few. In this paper, we address the problem of generating paraphrases automatically. Our proposed method is based on a combination of deep generative models (VAE) with sequence-to-sequence models (LSTM) to generate paraphrases, given an input sentence. Traditional VAEs when combined with recurrent neural networks can generate free text but they are not suitable for paraphrase generation for a given sentence. We address this problem by conditioning the both, encoder and decoder sides of VAE, on the original sentence, so that it can generate the given sentence’s paraphrases. Unlike most existing models, our model is simple, modular and can generate multiple paraphrases, for a given sentence. Quantitative evaluation of the proposed method on a benchmark paraphrase dataset demonstrates its efficacy, and its performance improvement over the state-of-the-art methods by a significant margin, whereas qualitative human evaluation indicate that the generated paraphrases are well-formed, grammatically correct, and are relevant to the input sentence. Furthermore, we evaluate our  method on a newly released question paraphrase dataset, and establish a new baseline for future research."
  res=translate(b)
  print(res)
