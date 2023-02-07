<hr>
<h2>Welcome to the AirBnB clone project!</h2>
<h3>Description of the project</h3>
<h6>This is the first step towards building your first full web application: the AirBnB clone</h6>
<h3>Description of the command interpreter</h3>
<ul>
<li>Retrieve an object from a file, a database etc…</li>
<li>Do operations on objects (count, compute stats, etc…)</li>
<li>Update attributes of an object</li>
<li>Destroy an object
FileStorage
The default mode.</li>
</ul>
<h3>How to Start it</h3>
<p>creates an instance of FileStorage named storage whenever the backend is initialized in FileStorage mode. The JSON file file.json’s class instances are used to load and reload the storage object. The storage object is used to record changes in the file as class instances are created, updated, or removed. json.</p>
<h3>How to use it</h3>
<p>Using the Console
Both interactive and non-interactive modes of the console can be used. Pipe any command(s) into an execution of the <a href="http://console.py">console.py</a> file at the command line to execute the console in a non-interactive mode.</p>
<p>$ echo “help” | ./console.py
(hbnb)</p>
<p>EOF  all  count  create  destroy  help  quit  show  update</p>
<p>(hbnb)
$
Alternatively, to use the HolbertonBnB console in interactive mode, run the file <a href="http://console.py">console.py</a> by itself:</p>
<p>$ ./console.py
While running in interactive mode, the console displays a prompt for input:</p>
<p>$ ./console.py
(hbnb)
To quit the console, enter the command quit, or input an EOF signal (ctrl-D).</p>
<p>$ ./console.py
(hbnb) quit
$
$ ./console.py
(hbnb) EOF
$</p>
<h3>Examples</h3>
<p>The console supports the following commands:
create</p>
<ul>
<li>Usage: create &lt;class&gt; &lt;param 1 name&gt;=&lt;param 1 value&gt; &lt;param 2 name&gt;=&lt;param 2 value&gt; …</li>
</ul>
<p>$ ./console.py
(hbnb) create BaseModel
119be863-6fe5-437e-a180-b9892e8746b8
(hbnb)
(hbnb) create State name=“Addis”
(hbnb) quit
$ cat file.json ; echo “”
{“BaseModel.119be863-6fe5-437e-a180-b9892e8746b8”: {“updated_at”: “2019-02-17T2
1:30:42.215277”, “created_at”: “2019-02-17T21:30:42.215277”, “<strong>class</strong>”: “Base
Model”, “id”: “119be863-6fe5-437e-a180-b9892e8746b8”}, {‘id’: ‘d80e0344-63eb-43
4a-b1e0-07783522124e’, ‘created_at’: datetime.datetime(2017, 11, 10, 4, 41, 7,
842160), ‘updated_at’: datetime.datetime(2017, 11, 10, 4, 41, 7, 842235), 'name
