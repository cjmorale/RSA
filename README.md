# RSA
Python code to perform RSA (Rivest–Shamir–Adleman) public-key cryptosystem.

# Flask App
There is Flask app that performs the RSA encryption and decryption. To run the code locally use the following command

```python
python main.py
```

The code will be running at **0.0.0.0:8080**

# Google Cloud Function
Flask application is currently running on a google cloud function. Hence, all endpoints can be accessed at the following url

```python
https://us-central1-upbeat-legacy-250621.cloudfunctions.net/rsa
```

# Google Cloud Run
Flask application is also currently running on google cloud run. This service has a docker container hosting the app using **gunicorn**. The endpoint can be accessed here.
```json
https://rsa-ebqmominqa-uc.a.run.app
```
# Kubernetes Engine
Flask app is also running on a Kubernetes cluster within the google cloud platform. The endpoints can be accessed here.
```json
35.184.69.7:8080
```
If this endpoint is down and you would like to use it please email Carlo Morales at *cjmorale2004@gmail.com*

# Tests
To run the pytest test suite run the following code while in the main project directory.

```json
pytest --cov-report term-missing --cov=RSA
```

# Endpoints
### /create_key

This endpoint accepts post requests. You must send a json object with the following fields.

- length_p: length of first prime
- length_q: length of second prime
- length_q: length of encryption exponenet

We recommend using primes larger than 100 digits.

#### Example
If we sent this JSON object
```json
{
	"length_p": 150,
	"length_q": 100,
	"length_e": 10
}
```
we get back the following
```json
{
	"q": 4038748597381937556833217040420222788726117750270025416853835411860720071714480754296099134659081513,
	"e": 7912416613,
	"p": 567410833838074456967844116944596705182098030941655820205154731004886910139108165010642221629118053436291782065511207091451073066361427748777481242911,
	"d": 469053967701680487391218454165227928863617265543325041998656486782645220586261103507664739696185230261548081884200091726626437172506249527623795229995752526834875832746930114845084457142155060434941351923189431835015812045819917956747767519318867357,
	"N": 2291629709302838845857229934937950623683020422270924117418629363327132328023333700408011220942118919000221515092649375006506694026930728842979026562406224624621192278265982531512554851334829666899007232990546301093827432804529395125636976980902404343
}
```

This JSON contains the following

- N: public modulus
- d: private deryption key (keep secret)
- e: encryption exponenet
- p: first prime
- q: second prime

### /encrypt

This endpoint accepts post requests. You must send a json object with the following fields.

- messege: messege to encrypt
- N: public modulus
- e: encryption exponenet

Note that N and e are ment to be public so anyone can send an encrypted message

#### Example

If we sent the following json

```json
{
	"message": "This is a message.",
	"e": 7912416613,
	"N": 2291629709302838845857229934937950623683020422270924117418629363327132328023333700408011220942118919000221515092649375006506694026930728842979026562406224624621192278265982531512554851334829666899007232990546301093827432804529395125636976980902404343
}
```

we get back a list of large integers which is the encrypted message

```json
[
  831645796399872061388606346190367511682330286555795322306776835687878131234457671834697189278422629559570799277012831668330883143171547449242130510031708635498802361275681750585704887325257766296143899356800891500194893529197200051933226473774025408,
  55923921366485570609210137958583797762407572352741589789004041829357567572412319087898258652016066333431425685929812798245916027548807186267194451618105465005505975292062045251040115454211097610697372293456659586166059674806562203126514898312545358,
  2273014466924021484072674923909822062289945112114387979079360139985242470277112648876960262106888239450425289675507486131219546807037921150733602757194661244226494416062990448686443790503030492474998371518779632889556874775953196857956983274898322351,
  975639711144378068538688542928702817002817440224451149378628433131848217618289618565994015129597559439116230806054924974797410715144987240532955656065026910639209604097731957396574143173497361824672571779935229434851973972735175598690231975098437684,
  0,
  2273014466924021484072674923909822062289945112114387979079360139985242470277112648876960262106888239450425289675507486131219546807037921150733602757194661244226494416062990448686443790503030492474998371518779632889556874775953196857956983274898322351,
  975639711144378068538688542928702817002817440224451149378628433131848217618289618565994015129597559439116230806054924974797410715144987240532955656065026910639209604097731957396574143173497361824672571779935229434851973972735175598690231975098437684,
  0,
  2289107758503811315127405482436080194233544394267764188305035912093576254398794219059935555714287801398751978569216382936064600866003612479031244007683727503906686830666121303227111574315162986598815485013658654909424871674704772304252206943689715041,
  0,
  1808687392536252359827852404499692365794415254598311255974670385113270198732460509615299550810553095825320560334505381854036933541888212870960645599061860688238734690825254167409513874118020668303540662432728102803839680528987405549153862911393315666,
  2004191627425279234970244508354129674762105696024786070106700261715212055524795755246014835063158984670853182909326992306608109154154088333275695969001180773547141105066991257516079965022774148802150104209201791676367575501396391514918154804753603493,
  975639711144378068538688542928702817002817440224451149378628433131848217618289618565994015129597559439116230806054924974797410715144987240532955656065026910639209604097731957396574143173497361824672571779935229434851973972735175598690231975098437684,
  1509126485697733485503945358434871327467402550247243242245548366239592184190081159017719774074131776206462907010660193793718963226857784387412542035925260975416494087234356781285261983856454452435561538073941571888660614862070706529015171226302721,
  2289107758503811315127405482436080194233544394267764188305035912093576254398794219059935555714287801398751978569216382936064600866003612479031244007683727503906686830666121303227111574315162986598815485013658654909424871674704772304252206943689715041,
  845762265209352116713911173915119498145966369251207333797746050431346402422010046999285918283569578599765302077913776478968545016749682150680980175961441963961669541276464195295678320849193065027075420304615243377022975823312610294035330235154702512,
  509215900937189636864802066439087902133518261956258795569063508039974527699641620245288401854997833577138614506033460109452379460561893845421215542373358716058669104012782505455621194426245628399960982591598865686521308611599558456107419685270683865,
  1816235079627102123527186659283732615706718636675690437171771062745863444511519585552016330885895357446985759064159632982187164088607616444072759705718842316578762345318636878669466489336377936829185603795672598469721149947189813411011671554624937967
]
```
Each element of the list is the encoded text using the built in padding scheme.

### /decrypt
This JSON contains the following

- encrypted: list of encoded integers
- N: public modulus
- d: private deryption key (the key you keep secret)


Below is an example of a proper JSON payload for this endpoint. The only way someone could decode the message is by having the decryption exponenet **d**. The only way to find **d** is to factor N which is computational infeasible if we pick large enough primes **p** and **q**

```json
{
	"encrypted": [
		831645796399872061388606346190367511682330286555795322306776835687878131234457671834697189278422629559570799277012831668330883143171547449242130510031708635498802361275681750585704887325257766296143899356800891500194893529197200051933226473774025408,
		55923921366485570609210137958583797762407572352741589789004041829357567572412319087898258652016066333431425685929812798245916027548807186267194451618105465005505975292062045251040115454211097610697372293456659586166059674806562203126514898312545358,
		2273014466924021484072674923909822062289945112114387979079360139985242470277112648876960262106888239450425289675507486131219546807037921150733602757194661244226494416062990448686443790503030492474998371518779632889556874775953196857956983274898322351,
		975639711144378068538688542928702817002817440224451149378628433131848217618289618565994015129597559439116230806054924974797410715144987240532955656065026910639209604097731957396574143173497361824672571779935229434851973972735175598690231975098437684,
		0,
		2273014466924021484072674923909822062289945112114387979079360139985242470277112648876960262106888239450425289675507486131219546807037921150733602757194661244226494416062990448686443790503030492474998371518779632889556874775953196857956983274898322351,
		975639711144378068538688542928702817002817440224451149378628433131848217618289618565994015129597559439116230806054924974797410715144987240532955656065026910639209604097731957396574143173497361824672571779935229434851973972735175598690231975098437684,
		0,
		2289107758503811315127405482436080194233544394267764188305035912093576254398794219059935555714287801398751978569216382936064600866003612479031244007683727503906686830666121303227111574315162986598815485013658654909424871674704772304252206943689715041,
		0,
		1808687392536252359827852404499692365794415254598311255974670385113270198732460509615299550810553095825320560334505381854036933541888212870960645599061860688238734690825254167409513874118020668303540662432728102803839680528987405549153862911393315666,
		2004191627425279234970244508354129674762105696024786070106700261715212055524795755246014835063158984670853182909326992306608109154154088333275695969001180773547141105066991257516079965022774148802150104209201791676367575501396391514918154804753603493,
		975639711144378068538688542928702817002817440224451149378628433131848217618289618565994015129597559439116230806054924974797410715144987240532955656065026910639209604097731957396574143173497361824672571779935229434851973972735175598690231975098437684,
		1509126485697733485503945358434871327467402550247243242245548366239592184190081159017719774074131776206462907010660193793718963226857784387412542035925260975416494087234356781285261983856454452435561538073941571888660614862070706529015171226302721,
		2289107758503811315127405482436080194233544394267764188305035912093576254398794219059935555714287801398751978569216382936064600866003612479031244007683727503906686830666121303227111574315162986598815485013658654909424871674704772304252206943689715041,
		845762265209352116713911173915119498145966369251207333797746050431346402422010046999285918283569578599765302077913776478968545016749682150680980175961441963961669541276464195295678320849193065027075420304615243377022975823312610294035330235154702512,
		509215900937189636864802066439087902133518261956258795569063508039974527699641620245288401854997833577138614506033460109452379460561893845421215542373358716058669104012782505455621194426245628399960982591598865686521308611599558456107419685270683865,
		1816235079627102123527186659283732615706718636675690437171771062745863444511519585552016330885895357446985759064159632982187164088607616444072759705718842316578762345318636878669466489336377936829185603795672598469721149947189813411011671554624937967
	],
	"d": 469053967701680487391218454165227928863617265543325041998656486782645220586261103507664739696185230261548081884200091726626437172506249527623795229995752526834875832746930114845084457142155060434941351923189431835015812045819917956747767519318867357,
	"N": 2291629709302838845857229934937950623683020422270924117418629363327132328023333700408011220942118919000221515092649375006506694026930728842979026562406224624621192278265982531512554851334829666899007232990546301093827432804529395125636976980902404343
}
```

Sending this to the endpoint would result in the following.

```json
"This is a message."
```
