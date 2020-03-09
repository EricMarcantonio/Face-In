<h1 id="welcome-to-faceit">Welcome to FaceIt</h1>
<p><strong>FaceIt</strong> is a open source project, dedicated to helping businesses and companies verify and check in human beings using Facial Recognition and some intuition</p>
<h1 id="in-a-nutshell">In a nutshell</h1>
<h3 id="we-found-a-problem-that-needed-a-cost-effective-solution">We found a problem, that needed a cost-effective solution</h3>
<p><strong>FaceIt</strong> was created because we (the human developers) could not find a free and (almost)<br>
pre-packaged Facial Recognition Software. So we made one ourselves! And lets FaceIt, who doesn’t like free?</p>
<h1 id="technical">Technical</h1>
<h2 id="installation">Installation</h2>
<h3 id="for-everyday-humans">For Everyday humans</h3>
<p>We created this software for more then just use by a developer. The idea behind this project was to allow people to utilize Machine Learning and AI, without having to code it! Just supply the faces, names and a test photo, and your done!</p>
<h3 id="for-developers">For Developers</h3>
<p>As fellow developers, we hope you enjoy this project (it was a lot of “fun” to make).</p>
<h4 id="software-stack">Software stack</h4>
<p>For the packaging and shipping of software, we used docker (containerization seemed appropriate, based on the target audience).</p>
<pre><code>docker install FaceIt or something idk yet
</code></pre>
<p>If you really want to customize this project, we suggest that you for the repo, and work on it yourself. Here is some help with the project structure:</p>
<h5 id="python-main.py"><code>python main.py</code></h5>
<p>This is the main program. At the moment it is under renovation, as to what it does. Right now, it trains the model, and identifies everyone in the test_pics folder</p>
<h5 id="preprocessdata">PreProcessData</h5>
<p>This file folder contains all the nessasary code to</p>
<ol>
<li>Identify a face in a photo</li>
<li>Crop, and resize the face</li>
<li>Use Google’s open source FaceNet model, to derive the embedding of each face</li>
<li>Create a SVC model and train it based on the pictures in rawData</li>
<li>Save a pre-trained model for quick photo analysis</li>
</ol>
<p>Pretty cool right? Each “part” is seperated into folders, and is heavily commeneted, so it should be (hopefully) easier to understand how the program runs.</p>
<h2 id="rename-a-file">Rename a file</h2>
<p>You can rename the current file by clicking the file name in the navigation bar or by clicking the <strong>Rename</strong> button in the file explorer.</p>
<h2 id="delete-a-file">Delete a file</h2>
<p>You can delete the current file by clicking the <strong>Remove</strong> button in the file explorer. The file will be moved into the <strong>Trash</strong> folder and automatically deleted after 7 days of inactivity.</p>
<h2 id="export-a-file">Export a file</h2>
<p>You can export the current file by clicking <strong>Export to disk</strong> in the menu. You can choose to export the file as plain Markdown, as HTML using a Handlebars template or as a PDF.</p>
<h1 id="synchronization">Synchronization</h1>
<p>Synchronization is one of the biggest features of StackEdit. It enables you to synchronize any file in your workspace with other files stored in your <strong>Google Drive</strong>, your <strong>Dropbox</strong> and your <strong>GitHub</strong> accounts. This allows you to keep writing on other devices, collaborate with people you share the file with, integrate easily into your workflow… The synchronization mechanism takes place every minute in the background, downloading, merging, and uploading file modifications.</p>
<p>There are two types of synchronization and they can complement each other:</p>
<ul>
<li>
<p>The workspace synchronization will sync all your files, folders and settings automatically. This will allow you to fetch your workspace on any other device.</p>
<blockquote>
<p>To start syncing your workspace, just sign in with Google in the menu.</p>
</blockquote>
</li>
<li>
<p>The file synchronization will keep one file of the workspace synced with one or multiple files in <strong>Google Drive</strong>, <strong>Dropbox</strong> or <strong>GitHub</strong>.</p>
<blockquote>
<p>Before starting to sync files, you must link an account in the <strong>Synchronize</strong> sub-menu.</p>
</blockquote>
</li>
</ul>
<h2 id="open-a-file">Open a file</h2>
<p>You can open a file from <strong>Google Drive</strong>, <strong>Dropbox</strong> or <strong>GitHub</strong> by opening the <strong>Synchronize</strong> sub-menu and clicking <strong>Open from</strong>. Once opened in the workspace, any modification in the file will be automatically synced.</p>
<h2 id="save-a-file">Save a file</h2>
<p>You can save any file of the workspace to <strong>Google Drive</strong>, <strong>Dropbox</strong> or <strong>GitHub</strong> by opening the <strong>Synchronize</strong> sub-menu and clicking <strong>Save on</strong>. Even if a file in the workspace is already synced, you can save it to another location. StackEdit can sync one file with multiple locations and accounts.</p>
<h2 id="synchronize-a-file">Synchronize a file</h2>
<p>Once your file is linked to a synchronized location, StackEdit will periodically synchronize it by downloading/uploading any modification. A merge will be performed if necessary and conflicts will be resolved.</p>
<p>If you just have modified your file and you want to force syncing, click the <strong>Synchronize now</strong> button in the navigation bar.</p>
<blockquote>
<p><strong>Note:</strong> The <strong>Synchronize now</strong> button is disabled if you have no file to synchronize.</p>
</blockquote>
<h2 id="manage-file-synchronization">Manage file synchronization</h2>
<p>Since one file can be synced with multiple locations, you can list and manage synchronized locations by clicking <strong>File synchronization</strong> in the <strong>Synchronize</strong> sub-menu. This allows you to list and remove synchronized locations that are linked to your file.</p>
<h1 id="publication">Publication</h1>
<p>Publishing in StackEdit makes it simple for you to publish online your files. Once you’re happy with a file, you can publish it to different hosting platforms like <strong>Blogger</strong>, <strong>Dropbox</strong>, <strong>Gist</strong>, <strong>GitHub</strong>, <strong>Google Drive</strong>, <strong>WordPress</strong> and <strong>Zendesk</strong>. With <a href="http://handlebarsjs.com/">Handlebars templates</a>, you have full control over what you export.</p>
<blockquote>
<p>Before starting to publish, you must link an account in the <strong>Publish</strong> sub-menu.</p>
</blockquote>
<h2 id="publish-a-file">Publish a File</h2>
<p>You can publish your file by opening the <strong>Publish</strong> sub-menu and by clicking <strong>Publish to</strong>. For some locations, you can choose between the following formats:</p>
<ul>
<li>Markdown: publish the Markdown text on a website that can interpret it (<strong>GitHub</strong> for instance),</li>
<li>HTML: publish the file converted to HTML via a Handlebars template (on a blog for example).</li>
</ul>
<h2 id="update-a-publication">Update a publication</h2>
<p>After publishing, StackEdit keeps your file linked to that publication which makes it easy for you to re-publish it. Once you have modified your file and you want to update your publication, click on the <strong>Publish now</strong> button in the navigation bar.</p>
<blockquote>
<p><strong>Note:</strong> The <strong>Publish now</strong> button is disabled if your file has not been published yet.</p>
</blockquote>
<h2 id="manage-file-publication">Manage file publication</h2>
<p>Since one file can be published to multiple locations, you can list and manage publish locations by clicking <strong>File publication</strong> in the <strong>Publish</strong> sub-menu. This allows you to list and remove publication locations that are linked to your file.</p>
<h1 id="markdown-extensions">Markdown extensions</h1>
<p>StackEdit extends the standard Markdown syntax by adding extra <strong>Markdown extensions</strong>, providing you with some nice features.</p>
<blockquote>
<p><strong>ProTip:</strong> You can disable any <strong>Markdown extension</strong> in the <strong>File properties</strong> dialog.</p>
</blockquote>
<h2 id="smartypants">SmartyPants</h2>
<p>SmartyPants converts ASCII punctuation characters into “smart” typographic punctuation HTML entities. For example:</p>

<table>
<thead>
<tr>
<th></th>
<th>ASCII</th>
<th>HTML</th>
</tr>
</thead>
<tbody>
<tr>
<td>Single backticks</td>
<td><code>'Isn't this fun?'</code></td>
<td>‘Isn’t this fun?’</td>
</tr>
<tr>
<td>Quotes</td>
<td><code>"Isn't this fun?"</code></td>
<td>“Isn’t this fun?”</td>
</tr>
<tr>
<td>Dashes</td>
<td><code>-- is en-dash, --- is em-dash</code></td>
<td>– is en-dash, — is em-dash</td>
</tr>
</tbody>
</table><h2 id="katex">KaTeX</h2>
<p>You can render LaTeX mathematical expressions using <a href="https://khan.github.io/KaTeX/">KaTeX</a>:</p>
<p>The <em>Gamma function</em> satisfying <span class="katex--inline"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">Γ</mi><mo stretchy="false">(</mo><mi>n</mi><mo stretchy="false">)</mo><mo>=</mo><mo stretchy="false">(</mo><mi>n</mi><mo>−</mo><mn>1</mn><mo stretchy="false">)</mo><mo stretchy="false">!</mo><mspace width="1em"></mspace><mi mathvariant="normal">∀</mi><mi>n</mi><mo>∈</mo><mi mathvariant="double-struck">N</mi></mrow><annotation encoding="application/x-tex">\Gamma(n) = (n-1)!\quad\forall n\in\mathbb N</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mord">Γ</span><span class="mopen">(</span><span class="mord mathdefault">n</span><span class="mclose">)</span><span class="mspace" style="margin-right: 0.277778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.277778em;"></span></span><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mopen">(</span><span class="mord mathdefault">n</span><span class="mspace" style="margin-right: 0.222222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right: 0.222222em;"></span></span><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mord">1</span><span class="mclose">)</span><span class="mclose">!</span><span class="mspace" style="margin-right: 1em;"></span><span class="mord">∀</span><span class="mord mathdefault">n</span><span class="mspace" style="margin-right: 0.277778em;"></span><span class="mrel">∈</span><span class="mspace" style="margin-right: 0.277778em;"></span></span><span class="base"><span class="strut" style="height: 0.68889em; vertical-align: 0em;"></span><span class="mord mathbb">N</span></span></span></span></span> is via the Euler integral</p>
<p><span class="katex--display"><span class="katex-display"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">Γ</mi><mo stretchy="false">(</mo><mi>z</mi><mo stretchy="false">)</mo><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mi mathvariant="normal">∞</mi></msubsup><msup><mi>t</mi><mrow><mi>z</mi><mo>−</mo><mn>1</mn></mrow></msup><msup><mi>e</mi><mrow><mo>−</mo><mi>t</mi></mrow></msup><mi>d</mi><mi>t</mi> <mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mord">Γ</span><span class="mopen">(</span><span style="margin-right: 0.04398em;" class="mord mathdefault">z</span><span class="mclose">)</span><span class="mspace" style="margin-right: 0.277778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.277778em;"></span></span><span class="base"><span class="strut" style="height: 2.32624em; vertical-align: -0.91195em;"></span><span class="mop"><span style="margin-right: 0.44445em; position: relative; top: -0.001125em;" class="mop op-symbol large-op">∫</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 1.41429em;"><span class="" style="top: -1.78805em; margin-left: -0.44445em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">0</span></span></span><span class="" style="top: -3.8129em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">∞</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.91195em;"><span class=""></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.166667em;"></span><span class="mord"><span class="mord mathdefault">t</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height: 0.864108em;"><span class="" style="top: -3.113em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span style="margin-right: 0.04398em;" class="mord mathdefault mtight">z</span><span class="mbin mtight">−</span><span class="mord mtight">1</span></span></span></span></span></span></span></span></span><span class="mord"><span class="mord mathdefault">e</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height: 0.843556em;"><span class="" style="top: -3.113em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mathdefault mtight">t</span></span></span></span></span></span></span></span></span><span class="mord mathdefault">d</span><span class="mord mathdefault">t</span><span class="mspace" style="margin-right: 0.166667em;"></span><span class="mord">.</span></span></span></span></span></span></p>
<blockquote>
<p>You can find more information about <strong>LaTeX</strong> mathematical expressions <a href="http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference">here</a>.</p>
</blockquote>
<h2 id="uml-diagrams">UML diagrams</h2>
<p>You can render UML diagrams using <a href="https://mermaidjs.github.io/">Mermaid</a>. For example, this will produce a sequence diagram:</p>
<div class="mermaid"><svg xmlns="http://www.w3.org/2000/svg" id="mermaid-svg-Uh85VGRHRz83ztNz" height="100%" width="100%" style="max-width:750px;" viewBox="-50 -10 750 457"><g></g><g><line id="actor3" x1="75" y1="5" x2="75" y2="446" class="actor-line" stroke-width="0.5px" stroke="#999"></line><rect x="0" y="0" fill="#eaeaea" stroke="#666" width="150" height="65" rx="3" ry="3" class="actor"></rect><text x="75" y="32.5" style="text-anchor: middle;" dominant-baseline="central" alignment-baseline="central" class="actor"><tspan x="75" dy="0">Alice</tspan></text></g><g><line id="actor4" x1="275" y1="5" x2="275" y2="446" class="actor-line" stroke-width="0.5px" stroke="#999"></line><rect x="200" y="0" fill="#eaeaea" stroke="#666" width="150" height="65" rx="3" ry="3" class="actor"></rect><text x="275" y="32.5" style="text-anchor: middle;" dominant-baseline="central" alignment-baseline="central" class="actor"><tspan x="275" dy="0">Bob</tspan></text></g><g><line id="actor5" x1="475" y1="5" x2="475" y2="446" class="actor-line" stroke-width="0.5px" stroke="#999"></line><rect x="400" y="0" fill="#eaeaea" stroke="#666" width="150" height="65" rx="3" ry="3" class="actor"></rect><text x="475" y="32.5" style="text-anchor: middle;" dominant-baseline="central" alignment-baseline="central" class="actor"><tspan x="475" dy="0">John</tspan></text></g><defs><marker id="arrowhead" refX="5" refY="2" markerWidth="6" markerHeight="4" orient="auto"><path d="M 0,0 V 4 L6,2 Z"></path></marker></defs><defs><marker id="crosshead" markerWidth="15" markerHeight="8" orient="auto" refX="16" refY="4"><path fill="black" stroke="#000000" style="stroke-dasharray: 0px, 0px;" stroke-width="1px" d="M 9,2 V 6 L16,4 Z"></path><path fill="none" stroke="#000000" style="stroke-dasharray: 0px, 0px;" stroke-width="1px" d="M 0,1 L 6,7 M 6,1 L 0,7"></path></marker></defs><g><text x="175" y="93" style="text-anchor: middle;" class="messageText">Hello Bob, how are you?</text><line x1="75" y1="100" x2="275" y2="100" class="messageLine0" stroke-width="2" stroke="black" style="fill: none;" marker-end="url(#arrowhead)"></line></g><g><text x="375" y="128" style="text-anchor: middle;" class="messageText">How about you John?</text><line x1="275" y1="135" x2="475" y2="135" style="stroke-dasharray: 3px, 3px; fill: none;" class="messageLine1" stroke-width="2" stroke="black" marker-end="url(#arrowhead)"></line></g><g><text x="175" y="163" style="text-anchor: middle;" class="messageText">I am good thanks!</text><line x1="275" y1="170" x2="75" y2="170" style="stroke-dasharray: 3px, 3px; fill: none;" class="messageLine1" stroke-width="2" stroke="black" marker-end="url(#crosshead)"></line></g><g><text x="375" y="198" style="text-anchor: middle;" class="messageText">I am good thanks!</text><line x1="275" y1="205" x2="475" y2="205" class="messageLine0" stroke-width="2" stroke="black" style="fill: none;" marker-end="url(#crosshead)"></line></g><g><rect x="500" y="215" fill="#EDF2AE" stroke="#666" width="150" height="76" rx="0" ry="0" class="note"></rect><text x="496" y="239" fill="black" class="noteText"><tspan x="516" fill="black">Bob thinks a long</tspan></text><text x="496" y="253" fill="black" class="noteText"><tspan x="516" fill="black">long time, so long</tspan></text><text x="496" y="267" fill="black" class="noteText"><tspan x="516" fill="black">that the text does</tspan></text><text x="496" y="281" fill="black" class="noteText"><tspan x="516" fill="black">not fit on a row.</tspan></text></g><g><text x="175" y="319" style="text-anchor: middle;" class="messageText">Checking with John...</text><line x1="275" y1="326" x2="75" y2="326" style="stroke-dasharray: 3px, 3px; fill: none;" class="messageLine1" stroke-width="2" stroke="black"></line></g><g><text x="275" y="354" style="text-anchor: middle;" class="messageText">Yes... John, how are you?</text><line x1="75" y1="361" x2="475" y2="361" class="messageLine0" stroke-width="2" stroke="black" style="fill: none;"></line></g><g><rect x="0" y="381" fill="#eaeaea" stroke="#666" width="150" height="65" rx="3" ry="3" class="actor"></rect><text x="75" y="413.5" style="text-anchor: middle;" dominant-baseline="central" alignment-baseline="central" class="actor"><tspan x="75" dy="0">Alice</tspan></text></g><g><rect x="200" y="381" fill="#eaeaea" stroke="#666" width="150" height="65" rx="3" ry="3" class="actor"></rect><text x="275" y="413.5" style="text-anchor: middle;" dominant-baseline="central" alignment-baseline="central" class="actor"><tspan x="275" dy="0">Bob</tspan></text></g><g><rect x="400" y="381" fill="#eaeaea" stroke="#666" width="150" height="65" rx="3" ry="3" class="actor"></rect><text x="475" y="413.5" style="text-anchor: middle;" dominant-baseline="central" alignment-baseline="central" class="actor"><tspan x="475" dy="0">John</tspan></text></g></svg></div>
<p>And this will produce a flow chart:</p>
<div class="mermaid"><svg xmlns="http://www.w3.org/2000/svg" id="mermaid-svg-63gYbU8L6b5N4loG" width="100%" style="max-width: 500.9549789428711px;" viewBox="0 0 500.9549789428711 172.59999084472656"><g transform="translate(-12, -12)"><g class="output"><g class="clusters"></g><g class="edgePaths"><g class="edgePath" style="opacity: 1;"><path class="path" d="M120.4875176804892,78.23333358764648L179.31665802001953,49.94166564941406L255.2583236694336,49.94166564941406" marker-end="url(#arrowhead33)" style="fill:none"></path><defs><marker id="arrowhead33" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1px; stroke-dasharray: 1px, 0px;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M120.4875176804892,124.94999313354492L179.31665802001953,153.24166107177734L234.79998779296875,153.24166107177734" marker-end="url(#arrowhead34)" style="fill:none"></path><defs><marker id="arrowhead34" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1px; stroke-dasharray: 1px, 0px;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M315.1416549682617,49.94166564941406L360.59999084472656,49.94166564941406L408.70982831217043,79.48182589315182" marker-end="url(#arrowhead35)" style="fill:none"></path><defs><marker id="arrowhead35" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1px; stroke-dasharray: 1px, 0px;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M335.59999084472656,153.24166107177734L360.59999084472656,153.24166107177734L408.70982831217043,124.7015008280396" marker-end="url(#arrowhead36)" style="fill:none"></path><defs><marker id="arrowhead36" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1px; stroke-dasharray: 1px, 0px;"></path></marker></defs></g></g><g class="edgeLabels"><g class="edgeLabel" style="opacity: 1;" transform="translate(179.31665802001953,49.94166564941406)"><g transform="translate(-30.48332977294922,-13.358329772949219)" class="label"><foreignObject width="60.96665954589844" height="26.716659545898438"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel">Link text</span></div></foreignObject></g></g><g class="edgeLabel" style="opacity: 1;" transform=""><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" style="opacity: 1;" transform=""><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" style="opacity: 1;" transform=""><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node" style="opacity: 1;" id="A" transform="translate(71.91666412353516,101.5916633605957)"><rect rx="0" ry="0" x="-51.916664123535156" y="-23.35832977294922" width="103.83332824707031" height="46.71665954589844"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-41.916664123535156,-13.358329772949219)"><foreignObject width="83.83332824707031" height="26.716659545898438"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Square Rect</div></foreignObject></g></g></g><g class="node" style="opacity: 1;" id="B" transform="translate(285.19998931884766,49.94166564941406)"><circle x="-29.941665649414062" y="-23.35832977294922" r="29.941665649414062"></circle><g class="label" transform="translate(0,0)"><g transform="translate(-19.941665649414062,-13.358329772949219)"><foreignObject width="39.883331298828125" height="26.716659545898438"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Circle</div></foreignObject></g></g></g><g class="node" style="opacity: 1;" id="C" transform="translate(285.19998931884766,153.24166107177734)"><rect rx="5" ry="5" x="-50.400001525878906" y="-23.35832977294922" width="100.80000305175781" height="46.71665954589844"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-40.400001525878906,-13.358329772949219)"><foreignObject width="80.80000305175781" height="26.716659545898438"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Round Rect</div></foreignObject></g></g></g><g class="node" style="opacity: 1;" id="D" transform="translate(445.2774848937988,101.5916633605957)"><polygon points="59.677494049072266,0 119.35498809814453,-59.677494049072266 59.677494049072266,-119.35498809814453 0,-59.677494049072266" rx="5" ry="5" transform="translate(-59.677494049072266,59.677494049072266)"></polygon><g class="label" transform="translate(0,0)"><g transform="translate(-32.94999694824219,-13.358329772949219)"><foreignObject width="65.89999389648438" height="26.716659545898438"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Rhombus</div></foreignObject></g></g></g></g></g></g></svg></div>

