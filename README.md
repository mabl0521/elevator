<style>
h2 {color: blue;}>
</style>
<p>.This project developes the code for a model elevator of 2 cars runs on a raspberry pi 3 <br>
<br>
to clone <br>
-git clone https://github.com/sdev265/elevator.git<br>
<br>
HISTORY<br>
One year ago AHI funded the building of a tabletop model prototype. <br>
The general requirements was the prototype controller and software must control a five (5) floor elevator prototype. <br>
There was an understanding that project was likely to be more complex than initially anticipated.<br>
<br>
The prototype was constructed to discover and identify issues. <br>
The previous team confirmed that Raspberry Pi(s) are capable of controlling a prototype model elevator<br>
<br>
Current Status<br>
With the success of the prototype, AHI has agreed to continue funding the project to scale up the model and add features with a new team of developers. <br>
The model and software will implement as many “normal” passenger elevator functions as possible. <br>
<br>
</p>
<h2> MASTER (raspberry pi) </h2>

<p>
gets button presses<br>
Gets car location<br>
Maintain floor lists<br>
Send floor stop lists to cars<br>
Computes car movement priority <br>
</p>


<h2>CAR 1 control (raspberry pi) </h2>
<p>
Move car up/down<br>
Controls door<br>
Knows location<br>
Monitor floor button<br>
Turns lamp on/off<br>
Send car info to master<br>
Receives floor stop list from master<br>
</p>

<h2>CAR 2 control (Raspberry PI) </h2>
<p>
Move car up/down<br>
Controls door<br>
Knows location<br>
Monitor floor button<br>
Turns lamp on/off<br>
Send car info to master<br>
Receives floor stop list from master<br>
</p>

<h2>Monitor Hallway Buttons (Raspberry PI)</h2>
<p>
Controls Hall Way LAMP<br>
Send button info to master<br>
</p>