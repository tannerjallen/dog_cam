# Dog Monitoring Camera 🐶📷

Ever wonder if your pup is sneaking onto the couch while you're away? This project uses a Wyze camera broadcasting an RTSP feed, [YOLO real-time object detector](https://docs.ultralytics.com/models/yolo11/#overview), and a [dog training collar](https://a.co/d/4xBPpxn) to catch couch-surfing canines in the act. Monitor their mischief and win the battle of "No dogs on the couch!"

## Getting Started
1. Clone this repository.
2. Update the `config.json` file with your GPIO pins and RTSP feed URL.
3. Connect Raspberry Pi GPIO pins to control a dog training collar with a transistor.

## Usage
1. Run the `dog_monitor.py` script to launch the RTSP stream and start the object detector.
2. The system will beep and buzz the collar once at startup to confirm everything is working.
3. If a dog is detected on the couch, the program will beep the collar to remind them to stay off.
4. Each beep/buzz event is recorded in `beep_log.txt`.

## License
This project is licensed under the MIT License.

*Created by Tanner J. Allen 2025. See [tannerjallen.com](https://tannerjallen.com).*