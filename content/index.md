---
marp: true
size: 16:9
theme: bouvet
footer: AppSec Workshop - Content Security Policies
paginate: true
html: true  
---
<!-- _class: lead -->
![bg right:35%](./resources/bouvet_people.jpg)
# Content Security Policies<br>Workshop

```
Security isn’t something you buy, it’s something you do!
```

---
## Learning objectives 👩🏽‍🏫

- 👨🏼‍💻 Awareness and understanding of certain types of web app attacks
- 🐞 Exploring and learning Content Security Policies and how they can mitigate attacks
- 🤩 Inspire to increase understanding of Application Security (AppSec) 
- 🤗 Have fun while learning! 
---

# Agenda

```
- The risk of injections (XSS)
  - Top most dangrous software weaknesses
  - Why do we need CSP
- CSP directives - with a ☕️ break :
  - "default-src"
  - "script-src" - "style-src" - "font-src" - "img-src"
  - "connect-src" and "media-src"
- Reporting URI - logging violation issues
  - "report-uri / report-to" directive
- Applying directives to your existing project
- We explore together - by adding CSP to an existing site
```

---
# Disclaimer

- We're not experts but we're here together to learn and share what we have learned so far in the journey
- Application Security is a broad topic - this workshop has it's focus on CSP for defending for certain types of attacks
- The perspective is depended on experience, personal journey in security and many other factors
- The more we learn about cyber security, the more we realise how complex it is
- Please share your thoughts, ideas and experiences

---
<style scoped>
section h1 {
  font-size: 1.5rem;
  color: red;
  text-align: center;
}

</style>
# Warning ⚠️⚠️⚠️

- Warning: Please do not attempt to hack any computer system without legal permission to do so. Unauthorised computer hacking is illegal and can be punished
- Innbrudd i datasystem
  - Lovdata §204 https://lovdata.no/lov/2005-05-20-28/§204
  - _"Med bot eller fengsel inntil 2 år straffes den som ved å bryte en beskyttelse eller ved annen uberettiget fremgangsmåte skaffer seg tilgang til datasystem eller del av det"_

---
<style scoped>
section h1 {
  font-size: 12rem;
  color: red;
  text-align: center;
  
}
</style>

# &lt;

---
<style scoped>
section h1 {
  font-size: 14rem;
  color: red;
  text-align: center;
}
</style>

# XSS

---
<style scoped>
section code {
  text-align: left;
  font-size: 1.1rem;
  background-color:black;
  color: white;
  
}
section h1 {
  font-size: 3rem;
  color: red;
  text-align: center;
}
</style>

# 😬😳🫨🤯

`""[(!1+"")[3]+(!0+"")[2]+(''+{})[2]][(''+{})[5]+(''+{})[1]+((""[(!1+"")[3]+(!0+"")[2]+(''+{})[2]])+"")[2]+(!1+'')[3]+(!0+'')[0]+(!0+'')[1]+(!0+'')[2]+(''+{})[5]+(!0+'')[0]+(''+{})[1]+(!0+'')[1]](((!1+"")[1]+(!1+"")[2]+(!0+"")[3]+(!0+"")[1]+(!0+"")[0])+"(1)")()`

<!-- source: https://inventropy.us/blog/constructing-an-xss-vector-using-no-letters  -->

---
<style scoped>
section code {
  font-size: 1.2rem;
}
</style>

```javascript
Function("alert(1)")()
```
<!--# Function("alert(1)")(); -->
<!--# Function("alert(document.cookie)")(); -->

---

# Top Most Dangerous Software Weaknesses

1. Out-of-bounds Write - (overwrite memory - C/C++)
2. **Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')**
3. Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')

Source: [MITRE - cwe.mitre.org - 2023](https://cwe.mitre.org/top25/archive/2023/2023_top25_list.html)

---

# XSS - Cross-Site Scripting 

* Is a misnomer - Wrong name, nothing cross site about it
* A better name is "Java Script Injection" or "Content Injection"
* Easy to fix - difficult to fix at scale

---

# Why do we need CSP - 1 / 2

The primary goal of CSP is to mitigate and report XSS attacks!

* Content Security Policy (CSP) is an added layer of security
* XSS attacks exploit the browser's trust in the content received from the server
* Malicious scripts are executed by the victim's browser because the browser trusts the source of the content 

---

# Why do we need CSP - 2 / 2

* CSP helps to detect and mitigate certain types of attacks
  - Cross-Site Scripting (XSS) and data injection attacks
  - Attacks are used for data theft, site defacement, malware distribution etc.
* XSS ranked as 3rd on the OWASP TOP 10 list

---

# What is CSP?

From the W3C* definition :

>This [document](https://www.w3.org/TR/CSP3/#intro) defines Content Security Policy (CSP), a tool which developers can use to lock down their applications in various ways, mitigating the risk of content injection vulnerabilities such as cross-site scripting, and reducing the privilege with which their applications execute.

`*W3C = World Wide Web Consortium`

---

# Types of XSS attacks

There are several types of XSS:

|XSS      |-     |
|---------|------|
|Reflected|Type 1|
|Stored   |Type 2|
|DOM Based|Type 0|

`DOM = Document Object Model - W3C standard`

---

# Reflected XSS attack - 1 / 2

Reflected XSS occurs when user input is immediately returned by a web application in an error message, search result, or any other response that includes some or all of the input provided by the user as part of the request, without that data being made safe to render in the browser, and without permanently storing the user provided data.


Example:
```html
https://insecure-web.com/comment?message=<script src=https//evil.corp/badscript.js></script>
```

---

![bg 70%](./resources/reflected_xss_diagram.png)

---

# Stored (persistent) XSS attack

Stored XSS generally occurs when user input is stored on the target server, such as in a database, in a message forum, visitor log, comment field, etc. And then a victim is able to retrieve the stored data from the web application without that data being made safe to render in the browser.

 Instead of a decent comment on the blog's input field, the attacker write:
```html
<script src='https//evil.corp/badscript.js'/>
```

---

![bg 70%](./resources/stored_persistent_xss.png)

---

# Terms to help organize types of XSS - 1 / 2

* **Server XSS** - occurs when untrusted user supplied data is included in an HTTP response generated by the server. 
* **Client XSS** - occurs when untrusted user supplied data is used to update the DOM with an unsafe JavaScript call. A JavaScript call is considered unsafe if it can be used to introduce valid JavaScript into the DOM.

---
# Terms to help organize types of XSS - 2 / 2

|  XSS     |        Server          |       Client        | 
|----------|------------------------|---------------------|
| Stored   | Stored Server XSS      | Stored Client XSS   |
| Reflected| Reflected Server XSS   | Reflected Client XSS|

---

# How can we use CSP to mitigate XSS

##### HTTP Headers

`HTTP headers` let the client and the server pass additional information with an HTTP request or response.

- `Request headers` contain more information about the resource to be fetched, or about the client requesting the resource.
- `Response headers` hold additional information about the response, like its location or about the server providing it.

---
# HTTP Response headers -controls CSP directives

HTTP response headers<br>`Content-Security-Policy: <policy-directive>; <policy-directive>`

`Content-Security-Policy-Report-Only` header is useful for reporting, instead of only restricting. Useful for testing your webapp with CSPs.

---
# Content-Security-Policy - example

HTML Example:

```html
<meta http-equiv="Content-Security-Policy" content="default-src `none`;">
```

Python using Flask example:
```python
response.headers['Content-Security-Policy'] = "default-src 'none';"
response.headers['Content-Security-Policy-Report-Only'] = "default-src 'none';"

```
---

<!-- _class: lead -->

# Explore CSP directives

# `default-src` - `script-src`<br>`style-src` - `font-src` - `img-src`

---

# Directive : `default-src`

If a [`default-src`](https://www.w3.org/TR/CSP3/#directive-default-src) directive is present in a policy, its value will be used as the policy’s default source list. That is, given `default-src 'none';` `script-src 'self'`, script requests will use `'self'` as the source list to match against. Other requests will use `'none'`.

Example:
```python
response.headers['Content-Security-Policy'] = "default-src 'none';"
```

---

# Directive : `script-src`

The [script-src](https://www.w3.org/TR/CSP3/#directive-script-src) directive restricts the locations from which scripts may be executed. This includes not only URLs loaded directly into script elements, but also things like inline script blocks and XSLT stylesheets [XSLT] which can trigger script execution. 

Example:
```python
response.headers['Content-Security-Policy'] = "default-src 'none'; script-src 'self' https://js.bouvet.no <other_source>;"
```
---

# Directive : `style-src`

The [style-src](https://www.w3.org/TR/CSP3/#directive-style-src) directive restricts the locations from which style may be applied to a [Document](https://dom.spec.whatwg.org/#document).

Example:
```python
response.headers['Content-Security-Policy'] = "default-src 'none'; style-src 'self' https://css.bouvet.no <other_source>;"
```

---

# Directive : `font-src`

The [font-src](https://www.w3.org/TR/CSP3/#directive-font-src) directive specifies valid sources for fonts loaded using `@font-face`.

Example:
```python
response.headers['Content-Security-Policy'] = "default-src 'none'; script-src 'self'; style-src 'self'; font-src 'self' https://fonts.bouvet.no <other_source>; "
```

---

# Directive : `img-src`

The [img-src](https://www.w3.org/TR/CSP3/#directive-img-src) directive restricts the URLs from which image resources may be loaded.

Example:
```python
response.headers['Content-Security-Policy'] = "default-src 'none'; img-src 'self' https://images.bouvet.no <other_source>; "
```

---
<!-- _class: lead -->

# Explore directive<br>`connect-src` - `media-src`


---
# Directive : `connect-src`

The [connect-src](https://www.w3.org/TR/CSP3/#directive-connect-src) directive restricts the URLs which can be loaded using script interfaces. The APIs that are restricted are:
`<a> ping` - `fetch()` - `XMLHttpRequest` - `WebSocket` - `EventSource` and `Navigator.sendBeacon()`

Example:
```python
response.headers['Content-Security-Policy'] = "default-src 'none'; connect-src 'self' https://*.bouvet.no <other_source>;"
```
---
# Directive : `media-src`

The [media-src](https://www.w3.org/TR/CSP3/#directive-media-src) directive restricts the URLs from which `<video>`, `<audio>`, and associated text track resources may be loaded.

Example:
```python
response.headers['Content-Security-Policy'] = "default-src 'none'; media-src 'self' https://video.bouvet.no https://audio.bouvet.no <other_source>;"
```
---

<!-- _class: lead -->

# Reporting violations of directives<br>`report-uri` / `report-to`

---
# Directive : `report-uri` / `report-to`

[report-uri](https://www.w3.org/TR/CSP3/#directive-report-uri) is deprecated. However not all browsers support the new directive [report-to](https://www.w3.org/TR/CSP3/#directive-report-to), thus is ok to include both to support past and future browsers.

The [report-to](https://www.w3.org/TR/CSP3/#directive-report-to) directive defines a reporting endpoint to which violation reports ought to be sent. The endpoint must serve through the `https` protocol.

---
`report-to` example:
```python
response.headers['Reporting-Endpoints'] = "main-endpoint='https://bouvet.no/csp-reports';"

response.headers['Content-Security-Policy'] = "default-src 'none'; script-src 'self'; style-src 'self'; report-to: main-endpoint;"

response.headers['Content-Security-Policy'] = "default-src 'none'; report-uri https://bouvet.no/csp-reports;"

```
---
Example of violation report by the `report-to` directive
```json
[{
  "age":0,
  "body":{
	"blockedURL":"https://csplite.com/tst/media/7_del.png",
	"disposition":"enforce",
	"documentURL":"https://csplite.com/tst/test_frame.php?ID=229&hash=da964209653e467d337313e51876e27d",
	"effectiveDirective":"img-src",
	"lineNumber":9,
	"originalPolicy":"default-src 'none'; report-to endpoint-csp;",
	"referrer":"https://csplite.com/test229/",
	"sourceFile":"https://csplite.com/tst/test_frame.php?ID=229&hash=da964209653e467d337313e51876e27d",
	"statusCode":0
	},
  "type":"csp-violation",
  "url":"https://csplite.com/tst/test_frame.php?ID=229&hash=da964209653e467d337313e51876e27d",
  "user_agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}]
```
---
<!-- _class: lead -->

# Nonce and hashes

---
# Nonce - Inline script

Allowing all inline scripts is considered a security risk, so it's recommended to use a nonce-source or a hash-source instead. It is important to note, this nonce value needs to be dynamically generated as it has to be unique for each HTTP request.

```
<script nonce="2726c7f26c">
  const inline = 1;
  // …
</script>
```
`Content-Security-Policy: script-src 'nonce-2726c7f26c'`

---
# [Nonce - hijacking](https://www.w3.org/TR/CSP3/#security-nonce-hijacking)

* Your code : 
  `Content-Security-Policy: script-src 'nonce-abc'`
  ```html
  <p>Hello, [INJECTION POINT]</p>
  <script nonce="abc" src="/good.js"></script>
  ```

* If an attacker injects the string 

  ```html 
  "<script src='https://evil.com/evil.js' "  
  ````

---

- then the browser will receive the following:

  ```html
  <p>Hello, <script src='https://evil.com/evil.js' </p>
  <script nonce="abc" src="/good.js"></script>
  ```
It will then parse that code, ending up with a script element with a `src` attribute pointing to a malicious payload, an attribute named `</p>`, an attribute named `"<script"`, a nonce attribute, and a second src attribute which is helpfully discarded as duplicate by the parser.

---
# Hashes

Alternatively, you can create hashes from your inline scripts. CSP supports sha256, sha384 and sha512.
```
<script>
  const inline = 1;
</script>
```
`echo -n 'const inline = 1;' | openssl sha256 -binary | openssl base64`

`Content-Security-Policy: script-src 'sha256-2XA6OeWgx7rumjOswMWkHzvY7xYWT9JsRykQhkmJXi0='`

---
# Best practice

.. is ofc not to use inline scripts or styles, but use .js/.css files and hash files for use in CSP.

`cat ./scripts.js | openssl sha256 -binary | openssl base64`
`cat ./styles.css | openssl sha256 -binary | openssl base64`

`Content-Security-Policy: script-src 'sha256-47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU='; style-src 'sha256-yFzV7Vvcuayqdtl6O1dkcA1ivVe5RwOH6jLVDn83bfQ='`

---
# SRI Hash - `integrity`

Subresource Integrity (SRI) is a security feature that enables browsers to verify that resources they fetch (for example, from a CDN) are delivered without unexpected manipulation. It works by allowing you to provide a cryptographic hash that a fetched resource must match.

`<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" integrity="sha256-PDJQdTN7dolQWDASIoBVrjkuOEaI137FI15sqI3Oxu8=" crossorigin="anonymous">`

---
# report-uri.com

- Tools : https://report-uri.com/home/tools
- e.g. Scan security headers, Hashing etc
- SRI Hashes - https://report-uri.com/home/sri_hash
- There is also a service for storing your CSP errors for monitoring an analysis, ref. the `report-to` directive

---
<!-- _class: lead -->

# Applying directives to your<br>existing project

---

# Restrict and then adjust

1. Start with locking down everything
  `default-src='none';`
2. Set the directive to just report errors
  `Content-Security-Policy-Report-Only: default-src='none';`
3. Start adding directives - step by step
 `script-src` , `style-src`, `img-src` and `font-src`
4. Adjust directives iteratively, by interpreting errors in the console log

---
# Now you and your task 

- Restrict the url `/test` page with CSPs
- Have a look in the browser console for CSP errors
- Code in `/app/vuln_app.py`

```python
    #Set your HTTP Response headers below
    #response.headers['<header>'] = "<header_value(s)>"
    csp_policy = "default-src 'none';"
    script_policy = " script-src 'none';"
    style_policy = " style-src 'none';"
    font_policy = " font-src 'none';"
    img_policy = " img-src 'none';"
    response.headers['Content-Security-Policy-Report-Only'] = csp_policy
```