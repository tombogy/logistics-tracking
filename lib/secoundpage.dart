import 'package:flutter/material.dart';
import 'package:sagar/thirdscreen.dart';

class Secoundpage extends StatelessWidget {
  const Secoundpage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
        backgroundColor: Colors.yellow,
        title: Text("TITLE"),
      ),
      body: Center(
        child: ListView.builder(
            itemCount: 5,
            itemBuilder: (context, index) {
              return GestureDetector(
                onTap: () {
                  Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) => const Thirdpage()));
                },
                child: Container(
                  margin: EdgeInsets.only(
                      bottom: 20, top: 10, left: 10.0, right: 30.0),
                  height: 100,
                  width: 220,
                  color: Color.fromARGB(255, 160, 97, 92),
                ),
              );
            }),

        // ListView(
        //   scrollDirection: Axis.vertical,
        //   physics: AlwaysScrollableScrollPhysics(),
        //   shrinkWrap: true,
        //   children: [
        //     Container(
        //       margin: EdgeInsets.only(
        //           bottom: 20, top: 10, left: 10.0, right: 10.0),
        //       height: 50,
        //       width: 120,
        //       color: Colors.red,
        //     ),
        //     Container(
        //       margin: EdgeInsets.only(
        //           bottom: 20, top: 10, left: 10.0, right: 10.0),
        //       height: 50,
        //       width: 120,
        //       color: Colors.red,
        //     ),
        //     Container(
        //       margin: EdgeInsets.only(
        //           bottom: 20, top: 10, left: 10.0, right: 10.0),
        //       height: 50,
        //       width: 120,
        //       color: Colors.red,
        //     ),
        //     Container(
        //       margin: EdgeInsets.only(
        //           bottom: 20, top: 10, left: 10.0, right: 10.0),
        //       height: 50,
        //       width: 120,
        //       color: Colors.red,
        //     ),
        //     Container(
        //       margin: EdgeInsets.only(
        //           bottom: 20, top: 10, left: 10.0, right: 10.0),
        //       height: 50,
        //       width: 20,
        //       color: Colors.red,
        //     ),
        //     Container(
        //       margin: EdgeInsets.only(
        //           bottom: 20, top: 10, left: 10.0, right: 10.0),
        //       height: 50,
        //       width: 20,
        //       color: Colors.red,
        //     ),
        //   ],
        // ),
        //  Column(
        //   children: [
        //     Container(
        //       margin: EdgeInsets.only(bottom: 20, top: 10),
        //       height: 100,
        //       width: 220,
        //       color: Colors.green,
        //       child:
        // //       Column(
        //         mainAxisAlignment: MainAxisAlignment.center,
        //         children: [
        //           Text(
        //             "1.FUCK OFF",
        //             style: TextStyle(
        //                 fontSize: 30, fontWeight: FontWeight.bold),
        //           )
        //         ],
        //       ),
        //     ),
        //     Container(
        //       margin: EdgeInsets.only(bottom: 20, top: 10),
        //       height: 100,
        //       width: 220,
        //       color: Colors.red,
        //     ),
        //     Container(
        //       margin: EdgeInsets.only(bottom: 20, top: 10),
        //       height: 100,
        //       width: 220,
        //       color: Colors.blue,
        //     ),
        //     Container(
        //       margin: EdgeInsets.only(bottom: 20, top: 10),
        //       height: 100,
        //       width: 220,
        //       color: Colors.white,
        //     ),
        //   ],
        // ),
        // ),
      ),
      //   bottomSheet: Container(
      //       height: 200.0, child: Center(child: Text('bottom bar;'))),
      //   bottomNavigationBar: Container(
      //       color: Colors.blue,
      //       height: 100.0,
      //       child: Center(child: Text('bottam sheet'))),
    );
  }
}
