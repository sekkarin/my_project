import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:app_1/pages/fiistPage.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(home: fristPage(),);
  }
}
