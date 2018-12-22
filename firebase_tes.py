from firebase import firebase
firebase = firebase.FirebaseApplication('https://treadmill-b0a11.firebaseio.com/', None)
##result = firebase.get('/data',None)
result = firebase.post('/data',{'mode':'Recovery','time':'10:00:59','timestamp':'27/12/2018 01:04:00'})
print (result)