<h1> Sound Level Light Visualiseer </h1>

<h2>Overview</h2>
<p>
  This IoT app captures sounds using a USB/Bluetooth microphone and computes their decibel level. An LED adjusts its brightness according to the loudness of the sound. 
  I would imagine that this app would be beneficial to a person that suffers from severe hearing loss. The LED igonres any sound below 10 decibels and reaches peak brightness at 80 decibels. A higher decibel threshold can be set and demonstrated, but my neighbours wouldn`t support this.
</p>

<h2>Pictures and presentation videos</h2>

<img src="https://user-images.githubusercontent.com/45963302/115382355-3ee56f00-a1dd-11eb-9321-04b0cc34d424.png" width="500" height="400"/>
<img src="https://user-images.githubusercontent.com/45963302/115382360-40169c00-a1dd-11eb-8264-d81c70136ce3.png" width="400" height="500"/>
<a href="https://youtu.be/N6C9mG-UZEY">Presentation video</a>

<h2> Schematics Plan </h2>
<img src="https://user-images.githubusercontent.com/45963302/115400920-7ad6ff00-a1f2-11eb-801b-ffc68be465a0.png" width="400" height="500"/>
<h2> Pre-requisites  </h2>
<ul>
  <li>Raspberry pi 3 or 4</li>
  <li>USB/Bluetooth microphone input</li>
  <li>The following individual components:
    <ul>  
      <li>1 resistor</li>
      <li>1 LED</li>
      <li>2 male to female jumper wires</li>
      <li>1 breadboard</li>
    </ul>
  </li>
</ul>

<h2> Setup and Run  </h2>
<h3> Setup </h3>
<ul>
  <li>Flash an SD card with the <a href = "https://www.raspberrypi.org/software/operating-systems/#raspberry-pi-os-32-bit">Raspberry Pi OS</a>. The <i>desktop and recommended software </i>option should cover all the software dependencies
  <ul>
    <li> If you already have an OS flashed, then make sure that you have <i>python 3</i> and <i>pip</i> installed</li>
  </ul>
  <li>Install the PyAudio library (run ` pip install PyAudio `)</div> </li>
  <li>Connect the GPIO ports as the schematics above ( GPIO 17 and Ground ) </li>
  <li>Copy the .py file from this repo to the raspberry pi</li>
  <li>Connect a USB/Bluetooth micophone (or headphones that have a microphone) to the raspberry pi</li>
  <li>Make sure that the the device`s audio input comes from the microphone</li>
</ul>
<h3> Run </h3>
<ul>
  <li>Run the application either from an IDE or from the command line</li>
  <li>Enter the number of seconds for which you want it to run</li>
</ul>



