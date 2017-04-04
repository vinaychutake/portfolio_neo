

/*function chartload(data)
    {
    var canvas = document.getElementById("can");
    var ctx = canvas.getContext("2d");
    var lastend = 0;
    var data = data; // If you add more data values make sure you add more colors
    var myTotal = 0; // Automatically calculated so don't touch
    var myColor = ['red', 'green', 'blue','black']; // Colors of each slice
    var name = ['a','b','c'];

    for (var e = 0; e < data.length; e++) {
      myTotal += data[e];
    }

    for (var i = 0; i < data.length; i++) {
      ctx.fillStyle = myColor[i];
      ctx.beginPath();
      ctx.moveTo(canvas.width / 2, canvas.height / 2);
      // Arc Parameters: x, y, radius, startingAngle (radians), endingAngle (radians), antiClockwise (boolean)
      ctx.arc(canvas.width / 2, canvas.height / 2, canvas.height / 2, lastend, lastend + (Math.PI * 2 * (data[i] / myTotal)), false);
      ctx.lineTo(canvas.width / 2, canvas.height / 2);
      ctx.fill();
      lastend += Math.PI * 2 * (data[i] / myTotal);
    }
    }
*/

function wordcloudload(){
        try {
          TagCanvas.Start('myCanvas','tags',{
            textColour: '#ff0000',
            outlineColour: '#ff00ff',
            reverse: true,
            depth: 0.8,
            maxSpeed: 0.05
          });
        } catch(e) {
          // something went wrong, hide the canvas container
          document.getElementById('myCanvasContainer').style.display = 'none';
        }
      };
