import 'package:app_1/pages/login.dart';
import 'package:app_1/pages/register.dart';
import 'package:flutter/material.dart';

class fristPage extends StatefulWidget {
  @override
  _fristPageState createState() => _fristPageState();
}

class _fristPageState extends State<fristPage> {
  fnPrint() {
    return print("กดปุ่มแล้ว");
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        child: Padding(
          padding: EdgeInsets.fromLTRB(10, 0, 10, 10),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Image.asset(
                'assets/images/A.jpg',
                width: 400,
              ),
              Text(
                "บัญชีครัวเรือน",
                style: TextStyle(fontSize: 24),
              ),
              Text(
                "ระบบบริหารจัดการข้อมูลครัวเรือน",
                style: TextStyle(fontSize: 12),
              ),
              Text(
                "มหา................",
                style: TextStyle(fontSize: 12),
              ),
              Padding(
                padding: EdgeInsets.all(10),
              ),
              TextField(
                style: Theme.of(context).textTheme.body1,
                textAlign: TextAlign.start,
                decoration: InputDecoration(
                  labelText: 'Username',
                  icon: Icon(Icons.vpn_key),
                ),
                keyboardType: TextInputType.emailAddress,
              ),
              TextField(
                style: Theme.of(context).textTheme.bodyText1,
                textAlign: TextAlign.start,
                decoration: InputDecoration(
                  labelText: 'Password',
                  icon: Icon(Icons.vpn_key),
                ),
                keyboardType: TextInputType.emailAddress,
              ),
              Padding(
                padding: const EdgeInsets.fromLTRB(0, 20, 0, 0),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    RaisedButton(
                      onPressed: () => {
                        Navigator.push(context,
                            MaterialPageRoute(builder: (context) => login()))
                      },
                      child: Text('Login'),
                      color: Colors.blue,
                    ),
                    Padding(
                      padding: EdgeInsets.all(10),
                    ),
                    RaisedButton(
                      onPressed: () => {
                        Navigator.push(context,
                            MaterialPageRoute(builder: (context) => register()))
                      },
                      child: Text('Register'),
                    )
                  ],
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
