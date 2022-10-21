import 'package:flutter/material.dart';

class Blissful extends StatefulWidget {
  const Blissful({super.key});

  @override
  State createState() => BlissfulState();
}

class BlissfulState extends State<Blissful> {
  double _bliss = 0;

  @override
  Widget build(BuildContext context) {
    return SliderTheme(
      data: SliderTheme.of(context).copyWith(
          activeTrackColor: Colors.orange,
          inactiveTrackColor: Colors.blue,
          overlayColor: Colors.white),
      child: Slider(
        onChanged: (double value) {
          setState(() {
            _bliss = value;
          });
        },
        value: _bliss,
      ),
    );
  }
}
