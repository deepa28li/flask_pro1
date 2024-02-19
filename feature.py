from flask import Flask

FAI=Flask(__name__)

@FAI.route('/Stringresponse')
def Stringresponse():
    return 'We  are Dealing with First flask view...'

@FAI.route('/SecondStringresponse')
def SecondStringresponse():
    return 'We  are Dealing with second flask view...'

if __name__=='__main__':
    FAI.run(debug=True)