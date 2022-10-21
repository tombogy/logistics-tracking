import 'package:flutter/material.dart';

class Thirdpage extends StatelessWidget {
  const Thirdpage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.white,
        appBar: AppBar(
          backgroundColor: Colors.blue,
          centerTitle: true,
          title: Text(" third page"),
        ),
        body: GridView.builder(
            gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 10, mainAxisSpacing: 2.0, crossAxisSpacing: 2),
            itemCount: 100,
            itemBuilder: (context, index) {
              return Container(
                height: 5,
                width: 10,
                color: Colors.black,
              );
            }));

    //   Column(
    //     children: [
    //       Row(
    //         mainAxisAlignment: MainAxisAlignment.center,
    //         children: [
    //           Container(
    //             height: 150,
    //             width: 100,
    //             color: Colors.black,
    //           ),
    //           Container(
    //             margin: EdgeInsets.only(left: 10),
    //             height: 150,
    //             width: 100,
    //             color: Colors.black,
    //           ),
    //         ],
    //       ),
    //       Row(
    //         mainAxisAlignment: MainAxisAlignment.center,
    //         children: [
    //           Container(
    //             margin: EdgeInsets.only(top: 10, right: 5),
    //             height: 150,
    //             width: 100,
    //             color: Colors.black,
    //           ),
    //           Container(
    //             margin: EdgeInsets.only(top: 10, left: 5),
    //             height: 150,
    //             width: 100,
    //             color: Colors.black,
    //           ),
    //         ],
    //       ),
    //     ],
    //   ),
    // );
  }
}
