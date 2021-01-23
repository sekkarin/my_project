import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        // ++++++++++++++++++Appbar+++++++++++++++++
        appBar: AppBar(
          title: Text("HELLO WORLD"),
          backgroundColor: Colors.indigo.shade900,
          //action การแสดงปฏิกิริยา
          actions: <Widget>[
            IconButton(
              icon: Icon(Icons.settings),
              onPressed: null,
            ),
          ], //end action
          automaticallyImplyLeading: false,
          bottom: PreferredSize(
            preferredSize: const Size.fromHeight(5.0),
            child: Text(
              "สวัสดี user",
              textAlign: TextAlign.center,
            ),
          ),
        ),
        bottomNavigationBar: BottomAppBar(),

        // +++++++++++++++++++++body++++++++++++++
        body: Container(
          child: Text(
            'hello' +
                'world' +
                "adddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",
            textAlign: TextAlign.justify,
            style: TextStyle(
                fontSize: 24.0,
                fontStyle: FontStyle.italic,
                color: Colors.deepOrange[600],
                backgroundColor: Colors.black),
          ),
          padding: EdgeInsets.all(10.0),
          alignment: Alignment.topCenter,
        ),
      ),
    );
  }
}
