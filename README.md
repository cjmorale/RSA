# RSA
Python code to perform RSA (Rivest–Shamir–Adleman) public-key cryptosystems.

# Flask App
There is Flask app that performs the RSA encryption and decryption. To run the code locally use the folling command

```python
python app.py
```

The code will be running at **0.0.0.0:8080**

# Endpoints
### /create_key

This endpoint accepts post requests. You must send a json object with the following fields.

- length_p: length of first prime
- length_q: length of second prime
- length_q: length of encryption exponenet

We recommend using primes larger then 100 digits.

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
	"q": 2352189118900336699748518397285004267293785414491842167424627736929209258007419667658545415009164119,
	"d": 627711105437623172635928660156979098888610882718710450636300563856862790375588052115482834474520477337271802465296147462959801516857531227093017672781031037870560802962898305024428179475898011216169156652459551467958388249444356613010520142025568285,
	"p": 273554296422058479507265847298947158953915901306476881498799987429784818609548341434001348827724429631282348605927533757357005991293323928307049421059,
	"e": 8826035353,
	"N": 643451439472403263099280793702430269958861141624790077672192679462769438701155613756956191246892774401446212787798238786439815119759024817068305602148597978926455399664117601865930741456550835742891219095016682429418266163121660154362163918465782021
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

- messege: messege to ecrypt
- N: public modulus
- d: private deryption key (keep secret)
- e: encryption exponenet
- p: first prime
- q: second prime

#### Example

If we sent the following json

```json
{
	"messege": "This is a messege.",
	"q": 2352189118900336699748518397285004267293785414491842167424627736929209258007419667658545415009164119,
	"d": 627711105437623172635928660156979098888610882718710450636300563856862790375588052115482834474520477337271802465296147462959801516857531227093017672781031037870560802962898305024428179475898011216169156652459551467958388249444356613010520142025568285,
	"p": 273554296422058479507265847298947158953915901306476881498799987429784818609548341434001348827724429631282348605927533757357005991293323928307049421059,
	"e": 8826035353,
	"N": 643451439472403263099280793702430269958861141624790077672192679462769438701155613756956191246892774401446212787798238786439815119759024817068305602148597978926455399664117601865930741456550835742891219095016682429418266163121660154362163918465782021
}
```

we get back a list of large integers which is the encrypted messege

```json
[
  625893144739851460436360826069818107941312396989241782396342209597482000202743951328710973210918481764445591869482269891370039697922583051920766898775886021744675254945882237405121036958467050691931611105254120079282595377338788063242212602829640814,
  146933286076565098879650561246996288146839804312079774581964736215750197481894981050251709623739527522671454272142370867947899035246590754972165299059054430093900553037420459634791350247254758827299318778392431546475264285666610536553797926382362212,
  510281048977580107156209714591650307656741269262033299784861291924750311447219429501072123286538027403280591607814032967883287413675283895444403499520047330793498067874715286837317134990969346610084310034003377938862284890091097598241744588075105003,
  441380168808788855790519595824288836494021278333662141275711642468931126491996266744322989983237248081929943602764296636135911832949897831487456003930722945716114721226946270633762633430077648279958753966983473414382586474505448973524012192301242497,
  279784195737144819390563142837320300438355125885279090650985028426910959854721611845171826743014963549971266865029349186924982940050975797410533473234812784066947522602343306589915858424711836512755151918631486791593995080942484980540195080323016992,
  510281048977580107156209714591650307656741269262033299784861291924750311447219429501072123286538027403280591607814032967883287413675283895444403499520047330793498067874715286837317134990969346610084310034003377938862284890091097598241744588075105003,
  441380168808788855790519595824288836494021278333662141275711642468931126491996266744322989983237248081929943602764296636135911832949897831487456003930722945716114721226946270633762633430077648279958753966983473414382586474505448973524012192301242497,
  279784195737144819390563142837320300438355125885279090650985028426910959854721611845171826743014963549971266865029349186924982940050975797410533473234812784066947522602343306589915858424711836512755151918631486791593995080942484980540195080323016992,
  37002187926346531113683980453500035719641084081884396271692565998206778681384971927662836749443911544840256484751536317058263568926873658250892123837658812954372544323689561244490243918752948055293349596688792633753072175752775442140272556270442998,
  138901153344565912476191336938442338572607296145632901684165041227097378259441502725402722113594667281059020389605412272044101140111652227073918856784243639131414964025029423151670048353658349283528690631138536872750216753823910755247915142287432054,
  482910194438020716132533634033435864812809225419252970617149773477546824581916168869317054538611350907947036670350031573064697420102175667314345260863361898517625738828238667985479426886546771757348808305274996637421016343332722504775598745618936039,
  120075893910616514047040288349156084385156174785053782943503348809213519428407673539109758589349893810432636179710596449427128684459614869438646440163580492354085343238746831069518451688826443672404317946778665834277889379913256716299797981695722835,
  441380168808788855790519595824288836494021278333662141275711642468931126491996266744322989983237248081929943602764296636135911832949897831487456003930722945716114721226946270633762633430077648279958753966983473414382586474505448973524012192301242497,
  1639428931919261777247080687873689006947524457301874029386737647577444579510021669479387224088941067358550308299322515940099803829086660690939673166610751921945515414386315530941242707380235585782069288818802157354719058859163187261242033521730550,
  120075893910616514047040288349156084385156174785053782943503348809213519428407673539109758589349893810432636179710596449427128684459614869438646440163580492354085343238746831069518451688826443672404317946778665834277889379913256716299797981695722835,
  74543886065116187682588697950324403344569668278746926641063638904331144841934635872950115900605478895641158758731996791951400771758417895364326624745422465722541252084081374481028982301597405448178837829238111892068051491017052209562624949224158047,
  613978724707472444547726918165223334439635597631357223534722378174341565767792597099777035055824144292769248517972348522755194287236258597688759154220997174314093762525828605348407470804313167524386017207769465002841636383582144084942408893884530721,
  443784449030789510327289068962820393333873350138701233850612447282821702948377003393864186815423586632698498589896188595778156062150527682639365947662837427748868024362797789682450655475756714408597880360787324949981752709291504987190545626702363464
]


Each element of the list is the encoded text using the built in padding scheme.
```

### /decrypt
This JSON contains the following

- encrypted: list of encoded integers
- N: public modulus
- d: private deryption key (keep secret)
- e: encryption exponenet
- p: first prime
- q: second prime

Below is an example of a proper JSON payload for this endpoint

```json
{
"encrypted":[
  625893144739851460436360826069818107941312396989241782396342209597482000202743951328710973210918481764445591869482269891370039697922583051920766898775886021744675254945882237405121036958467050691931611105254120079282595377338788063242212602829640814,
  146933286076565098879650561246996288146839804312079774581964736215750197481894981050251709623739527522671454272142370867947899035246590754972165299059054430093900553037420459634791350247254758827299318778392431546475264285666610536553797926382362212,
  510281048977580107156209714591650307656741269262033299784861291924750311447219429501072123286538027403280591607814032967883287413675283895444403499520047330793498067874715286837317134990969346610084310034003377938862284890091097598241744588075105003,
  441380168808788855790519595824288836494021278333662141275711642468931126491996266744322989983237248081929943602764296636135911832949897831487456003930722945716114721226946270633762633430077648279958753966983473414382586474505448973524012192301242497,
  279784195737144819390563142837320300438355125885279090650985028426910959854721611845171826743014963549971266865029349186924982940050975797410533473234812784066947522602343306589915858424711836512755151918631486791593995080942484980540195080323016992,
  510281048977580107156209714591650307656741269262033299784861291924750311447219429501072123286538027403280591607814032967883287413675283895444403499520047330793498067874715286837317134990969346610084310034003377938862284890091097598241744588075105003,
  441380168808788855790519595824288836494021278333662141275711642468931126491996266744322989983237248081929943602764296636135911832949897831487456003930722945716114721226946270633762633430077648279958753966983473414382586474505448973524012192301242497,
  279784195737144819390563142837320300438355125885279090650985028426910959854721611845171826743014963549971266865029349186924982940050975797410533473234812784066947522602343306589915858424711836512755151918631486791593995080942484980540195080323016992,
  37002187926346531113683980453500035719641084081884396271692565998206778681384971927662836749443911544840256484751536317058263568926873658250892123837658812954372544323689561244490243918752948055293349596688792633753072175752775442140272556270442998,
  138901153344565912476191336938442338572607296145632901684165041227097378259441502725402722113594667281059020389605412272044101140111652227073918856784243639131414964025029423151670048353658349283528690631138536872750216753823910755247915142287432054,
  482910194438020716132533634033435864812809225419252970617149773477546824581916168869317054538611350907947036670350031573064697420102175667314345260863361898517625738828238667985479426886546771757348808305274996637421016343332722504775598745618936039,
  120075893910616514047040288349156084385156174785053782943503348809213519428407673539109758589349893810432636179710596449427128684459614869438646440163580492354085343238746831069518451688826443672404317946778665834277889379913256716299797981695722835,
  441380168808788855790519595824288836494021278333662141275711642468931126491996266744322989983237248081929943602764296636135911832949897831487456003930722945716114721226946270633762633430077648279958753966983473414382586474505448973524012192301242497,
  1639428931919261777247080687873689006947524457301874029386737647577444579510021669479387224088941067358550308299322515940099803829086660690939673166610751921945515414386315530941242707380235585782069288818802157354719058859163187261242033521730550,
  120075893910616514047040288349156084385156174785053782943503348809213519428407673539109758589349893810432636179710596449427128684459614869438646440163580492354085343238746831069518451688826443672404317946778665834277889379913256716299797981695722835,
  74543886065116187682588697950324403344569668278746926641063638904331144841934635872950115900605478895641158758731996791951400771758417895364326624745422465722541252084081374481028982301597405448178837829238111892068051491017052209562624949224158047,
  613978724707472444547726918165223334439635597631357223534722378174341565767792597099777035055824144292769248517972348522755194287236258597688759154220997174314093762525828605348407470804313167524386017207769465002841636383582144084942408893884530721,
  443784449030789510327289068962820393333873350138701233850612447282821702948377003393864186815423586632698498589896188595778156062150527682639365947662837427748868024362797789682450655475756714408597880360787324949981752709291504987190545626702363464
],
	"q": 2352189118900336699748518397285004267293785414491842167424627736929209258007419667658545415009164119,
	"d": 627711105437623172635928660156979098888610882718710450636300563856862790375588052115482834474520477337271802465296147462959801516857531227093017672781031037870560802962898305024428179475898011216169156652459551467958388249444356613010520142025568285,
	"p": 273554296422058479507265847298947158953915901306476881498799987429784818609548341434001348827724429631282348605927533757357005991293323928307049421059,
	"e": 8826035353,
	"N": 643451439472403263099280793702430269958861141624790077672192679462769438701155613756956191246892774401446212787798238786439815119759024817068305602148597978926455399664117601865930741456550835742891219095016682429418266163121660154362163918465782021
}
```

Sending this to the endpoint would result in the following.

```json
"This is a messege."
```