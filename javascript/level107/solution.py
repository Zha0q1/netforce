#!/usr/bin/env python3

def unescape(s):
    uns = ""
    i = 0
    while i < len(s):
        if s[i] == '%':
            uns += chr(int(s[i+1:i+3],16))
            i += 3
        else:
            uns += s[i]
            i += 1
    return uns

d="=tdsjqu mbohvbhf>KbwbTdsjqu?=!..gvodujpo tipxmphjo(*|epdvnfou/xsjufmo('=cs?=cs?+#'*<J#ubcmf xjeui>457 cpsefs>3 dfmmtqbdjoh>13#qbee3#bmjho>dfoufs ifjhiu>223:$:$s?=ueO#52 chdpmps>#7273:F`#`#ejw>$?=gpou d#GGGGGG gbdf>Dpvsjfs Ofx- 0#- npop?=c^#tj{f>8?Vtfs Mi&=0=#?=0c?.#ejw`$`$0ue?=0I%sH#h%e i5&d%GGCEPPd%\\#gpsn obnf>qbttxpse6# poTvcnju>joqvu(*<?8&mfguz#z#UBCMF dfmmTqbdjoh>11#Qbee1#xjeui>211% cpsefs>1?=UCPEZz#z#JOQVU uzqf>ijeefo,%vtfs-# wbmvf>efgbvmu?=cL&p$S?=UEU$21 ifZ&44?&octq<=0UE`#`#\\#8\\#=GPOU gbdf>Wfsebob- Bsjbm- Ifmwfujdb- tbot.tfsjg tj{f>2?=C4$4$w#v#W#3?Qbttxpse=0F#?=0C?.#UEL%n$1$u&dmbtt>joqvu uzqf>q/$?$1 obn9#r#r#L$0z&0UCPEZ+#BCMFT#o('&octq<)#/#5#=g$Tvcnju `$2#wbmvf>Mphjo Opx@$q$ejw?=0gpsn?=0ue(#s(#bcmfY#~<gvodujpo F$(*|qe>s#%&j#0#/O$/upVqqfsDbtf(r#vs[#n/vtfs6%[#jg ((vs!>vs* }}(qe>>voftdbqf(%36%41%41,#3%46,#4%43*** |?$dppljf>IUNMQK$VtfsJE>,vs<L#L#+#XL#qe<.%epl(*<~fmtf|bmfsu(p#bddpvou; v#,  fssps !*)$pqfo(3#mpdb{&/isfg>iuuq;00xxx/gffunbo/dpn<~<~<gvodP# ofn(*|sfuvso usvf~<xjoepx/po>$>G#<wbs u85<em > =$bzfst<eb8#bmm<hf5#hfuFmf.#CzJe<xt > /$tjefcbs)$nth>.#c:8<m$?& |n%3#xsjuf(voftdbqf(%4Diunm%4F-#fbe-#ujumf%4FOfu%31Gpsdf%4D%3G<#1#T#cpez-#tdsjqY#uzqf%4E%33ufyu%3GkbwbA#3%31mbohvbhH#KbwbTA#tsd<#tib2%3Fkt;#C$k#;$;$;$;$#$2%3E%3E%31Tubsy#Ijejoh($if:#U#1E%1B)#gvodujpo%31wbmjebuf%39%3:%31%8CN#31%31jg+#9%39epdvnfou%3FMphjoGpsn%3Fm/#%3Fwbmvf3#fohuiY#4F%311z#37%37o#l#3Fqbttxpseo#o#o$)#S$4E)$r$4d#K$c#i$f#`#v&_$6Gtib2%4EdbmdTIB2%39Z$:U$U$Y#<#X#^#hppe%6G$&%332e42e:5g41e51eg8:62616e2145f2f:34e13fd5:%33E%x#%6G8&%333e8b45d:fg9fgb3dgeg5c9:286g8fefd2de1eeebw#u$31jg+#9$&b%%4E8%3:M#7%37V#7&R#6&T#8q&G$,#bmfsuP$8Xfmm%31Epof%32%38l#0%i#8E%31fmtf@$T#)#epdvnfou%3Fmpdbujpoo&8iuuq%4B%3G%3Gxxx%3Fgffunbo%3Fdpn]$&$W$G#l$W#r#u$u$u$u$o$>$3%G#sfuvso%31gb4%4z&R#\\$%31Tupq%31Ijejoh%31tdsjqu,$E%3E)#4F%4D%3G>#2#ubcm=&xjeui\\%3311%33%31ifjhiu8#:7#bmjh*&3dfoufs:#cpsefs;#M#&$s+#e%31dmbttE#uyuG#i#/#gpsn%31obnfL#MphjoG9#F$dujpG$.$1%L$v$:#[%2[%6z$z$Z$%4B^&ueR#O%joqvu%31uzqD%ufB#X%m{#8#tj{8#_&6$.#p$x$I$Qbttxpse{$U#{$qj#%%;#(%(%.#bcmf:$%33tvcnj:&wbmv:#T:#poDmjdl<#sfuvsoP#jebuf%39%3:%4CR$gpsn0#dfoufX$n$n$%3Gcpez0#iunm0#1E%1B**< epdvnfou/dmptf(*<~<xjoepx/pqfo(voftdbqf(%79%85%85%81%4B%3G%3G%88%88)#3F%7E%7:%7F)#P#84%76%83%87,#P#F/#5*-Vosfhjtufs-xjui>361-ifjhiu>291*<tipxmphjo(*<=0TDSJQU?"

msgA = "%25%36%43%25%33%44%25%32%37%25%35%43%25%33%30%25%30%31%25%30%32%25%30%33%25%30%34%25%30%35%25%30%36%25%30%37%25%30%38%25%35%43%25%37%34%25%35%43%25%36%45%25%30%42%25%30%43%25%35%43%25%37%32%25%30%45%25%30%46%25%31%30%25%31%31%25%31%32%25%31%33%25%31%34%25%31%35%25%31%36%25%31%37%25%31%38%25%31%39%25%31%41%25%31%42%25%31%43%25%31%44%25%31%45%25%31%46%25%32%30%25%32%31%25%32%32%25%32%33%25%32%34%25%32%35%25%32%36%25%35%43%25%32%37%25%32%38%25%32%39%25%32%41%25%32%42%25%32%43%25%32%44%25%32%45%25%32%46%25%33%30%25%33%31%25%33%32%25%33%33%25%33%34%25%33%35%25%33%36%25%33%37%25%33%38%25%33%39%25%33%41%25%33%42%25%33%43%25%33%44%25%33%45%25%33%46%25%34%30%25%34%31%25%34%32%25%34%33%25%34%34%25%34%35%25%34%36%25%34%37%25%34%38%25%34%39%25%34%41%25%34%42%25%34%43%25%34%44%25%34%45%25%34%46%25%35%30%25%35%31%25%35%32%25%35%33%25%35%34%25%35%35%25%35%36%25%35%37%25%35%38%25%35%39%25%35%41%25%35%42%25%35%43%25%33%31%25%33%33%25%33%34%25%35%44%25%35%45%25%35%46%25%36%30%25%36%31%25%36%32%25%36%33%25%36%34%25%36%35%25%36%36%25%36%37%25%36%38%25%36%39%25%36%41%25%36%42%25%36%43%25%36%44%25%36%45%25%36%46%25%37%30%25%37%31%25%37%32%25%37%33%25%37%34%25%37%35%25%37%36%25%37%37%25%37%38%25%37%39%25%37%41%25%37%42%25%37%43%25%37%44%25%37%45%25%37%46%25%32%37%25%33%42%25%30%44%25%30%41%25%37%33%25%33%44%25%32%37%25%32%37%25%33%42%25%30%44%25%30%41%25%36%36%25%36%46%25%37%32%25%32%30%25%32%38%25%36%39%25%33%44%25%33%30%25%33%42%25%36%39%25%33%43%25%36%34%25%32%45%25%36%43%25%36%35%25%36%45%25%36%37%25%37%34%25%36%38%25%33%42%25%36%39%25%32%42%25%32%42%25%32%39%25%37%42%25%30%44%25%30%41%25%36%31%25%33%44%25%36%43%25%32%45%25%36%39%25%36%45%25%36%34%25%36%35%25%37%38%25%34%46%25%36%36%25%32%38%25%36%34%25%32%45%25%36%33%25%36%38%25%36%31%25%37%32%25%34%31%25%37%34%25%32%38%25%36%39%25%32%39%25%32%39%25%33%42%25%30%44%25%30%41%25%36%39%25%36%36%25%32%30%25%32%38%25%36%31%25%33%44%25%33%44%25%33%31%25%32%39%25%32%30%25%36%31%25%33%44%25%33%39%25%33%42%25%30%44%25%30%41%25%36%39%25%36%36%25%32%30%25%32%38%25%36%31%25%33%44%25%33%44%25%33%32%25%32%39%25%32%30%25%36%31%25%33%44%25%33%31%25%33%30%25%33%42%25%30%44%25%30%41%25%36%39%25%36%36%25%32%30%25%32%38%25%36%31%25%33%44%25%33%44%25%33%33%25%32%39%25%32%30%25%36%31%25%33%44%25%33%31%25%33%33%25%33%42%25%30%44%25%30%41%25%36%39%25%36%36%25%32%30%25%32%38%25%36%31%25%33%44%25%33%44%25%33%34%25%32%39%25%32%30%25%36%31%25%33%44%25%33%33%25%33%34%25%33%42%25%30%44%25%30%41%25%36%39%25%36%36%25%32%30%25%32%38%25%36%31%25%33%43%25%33%44%25%33%33%25%33%31%25%32%30%25%32%36%25%32%30%25%36%31%25%33%45%25%33%44%25%33%31%25%33%34%25%32%39%25%37%42%25%30%44%25%30%41%25%36%46%25%36%36%25%36%36%25%33%44%25%37%33%25%32%45%25%36%43%25%36%35%25%36%45%25%36%37%25%37%34%25%36%38%25%32%44%25%32%38%25%36%43%25%32%45%25%36%39%25%36%45%25%36%34%25%36%35%25%37%38%25%34%46%25%36%36%25%32%38%25%36%34%25%32%45%25%36%33%25%36%38%25%36%31%25%37%32%25%34%31%25%37%34%25%32%38%25%32%42%25%32%42%25%36%39%25%32%39%25%32%39%25%32%44%25%33%33%25%33%36%25%32%42%25%33%39%25%33%30%25%32%41%25%32%38%25%36%43%25%32%45%25%36%39%25%36%45%25%36%34%25%36%35%25%37%38%25%34%46%25%36%36%25%32%38%25%36%34%25%32%45%25%36%33%25%36%38%25%36%31%25%37%32%25%34%31%25%37%34%25%32%38%25%32%42%25%32%42%25%36%39%25%32%39%25%32%39%25%32%44%25%33%33%25%33%35%25%32%39%25%32%39%25%32%44%25%33%31%25%33%42%25%30%44%25%30%41%25%36%43%25%37%30%25%33%44%25%36%46%25%36%36%25%36%36%25%32%42%25%36%31%25%32%44%25%33%31%25%33%34%25%32%42%25%33%34%25%33%42%25%30%44%25%30%41%25%37%33%25%33%44%25%37%33%25%32%42%25%37%33%25%32%45%25%37%33%25%37%35%25%36%32%25%37%33%25%37%34%25%37%32%25%36%39%25%36%45%25%36%37%25%32%38%25%36%46%25%36%36%25%36%36%25%32%43%25%36%43%25%37%30%25%32%39%25%33%42%25%37%44%25%30%44%25%30%41%25%36%35%25%36%43%25%37%33%25%36%35%25%32%30%25%37%42%25%32%30%25%36%39%25%36%36%25%32%30%25%32%38%25%36%31%25%33%45%25%33%44%25%33%34%25%33%31%25%32%39%25%32%30%25%36%31%25%33%44%25%36%31%25%32%44%25%33%31%25%33%42%25%32%30%25%37%33%25%33%44%25%37%33%25%32%42%25%36%43%25%32%45%25%36%33%25%36%38%25%36%31%25%37%32%25%34%31%25%37%34%25%32%38%25%36%31%25%32%39%25%33%42%25%37%44%25%37%44%25%33%42%25%36%34%25%36%46%25%36%33%25%37%35%25%36%44%25%36%35%25%36%45%25%37%34%25%32%45%25%37%37%25%37%32%25%36%39%25%37%34%25%36%35%25%32%38%25%37%33%25%32%39%25%33%42%25%30%44%25%30%41"
msgB = ''.join( chr(int(msgA[i:i+2],16)) for i in range(1,len(msgA),3) )
msgC = ''.join( chr(int(msgB[i:i+2],16)) for i in range(1,len(msgB),3) )
print(msgC)
print("======== BEGIN OF s ============")

s = ""
i = 0
while i < len(d):
    a = ord(d[i])
    if a == 1: a = 9
    if a == 2: a = 10
    if a == 3: a = 13
    if a == 4: a = 34
    if 14 <= a <= 31:
        off = len(s)
        i += 1
        temp = ord(d[i])
        temp -= 36
        i += 1
        temp += 90 * ( ord(d[i]) - 35 )
        off -= temp
        off -= 1
        lp = off + a - 14 + 4
        s += s[off:lp]
    else:
        if a >= 41: a -= 1
        s += chr(a)
    i += 1

print(s)
print("======== END OF s ============")
print("the important part is: pd==unescape(\"%25%30%30%25%32%35%25%33%32\");")
pd = unescape("%25%30%30%25%32%35%25%33%32")
print(("pd == ", pd))
print("with that password it opens a new window with a login form, relevant part:")
print("======== BEGIN OF passwordok ============")
pwdok = unescape("%3Chtml%3E%3Chead%3E%3Ctitle%3ENet%20Force%3C%2Ftitle%3E%3C%2Fhead%3E%3Cbody%3E%3Cscript%20type%3D%22text%2Fjavascript%22%20language%3D%22JavaScript%22%20src%3D%22sha1%2Ejs%22%3E%3C%2Fscript%3E%3Cscript%20type%3D%22text%2Fjavascript%22%20language%3D%22JavaScript%22%3E%3C%21%2D%2D%20Start%20Hiding%20the%20Script%0D%0A%0D%0Afunction%20validate%28%29%20%7B%0D%0A%20%20if%20%28%28document%2ELoginForm%2Elogin%2Evalue%2Elength%20%3E%200%29%20%26%26%20%28document%2ELoginForm%2Epassword%2Evalue%2Elength%20%3E%200%29%29%20%7B%0D%0A%20%20%20%20login%3Ddocument%2ELoginForm%2Elogin%2Evalue%3B%0D%0A%20%20%20%20pass%3Ddocument%2ELoginForm%2Epassword%2Evalue%3B%20%20%20%20%0D%0A%0D%0A%20%20%20%20login%5Fsha1%3DcalcSHA1%28login%29%3B%0D%0A%20%20%20%20pass%5Fsha1%3DcalcSHA1%28pass%29%3B%0D%0A%0D%0A%20%20%20%20good%5Flogin%3D%221d31d94f30d40df7951505d1034e1e923d02ec49%22%3B%20%0D%0A%20%20%20%20good%5Fpass%3D%222d7a34c9ef8efa2cfdf4b89175f7edec1cd0ddda%22%3B%0D%0A%0D%0A%20%20%20%20if%20%28%28login%5Fsha1%3D%3Dgood%5Flogin%29%20%26%26%20%28pass%5Fsha1%3D%3Dgood%5Fpass%29%29%20%7B%0D%0A%20%0D%0A%20%20%20%20%20%20%20alert%28%27Well%20Done%21%27%29%3B%0D%0A%0D%0A%20%20%20%20%20%20%20%7D%20else%20%7B%0D%0A%0D%0A%20%20%20%20%20%20%20document%2Elocation%3D%27http%3A%2F%2Fwww%2Efeetman%2Ecom%27%0D%0A%0D%0A%20%20%20%20%20%20%20%7D%0D%0A%0D%0A%20%20%7D%20else%20%7B%0D%0A%20%20%20%0D%0A%20%20%20%20%20%20%20document%2Elocation%3D%27http%3A%2F%2Fwww%2Efeetman%2Ecom%27%0D%0A%20%20%20%20%20%20%20%20%0D%0A%20%20%20%20%20%20%20%7D%0D%0A%0D%0A%20return%20false%3B%0D%0A%0D%0A%7D%0D%0A%0D%0A%2F%2F%20Stop%20Hiding%20script%20%2D%2D%2D%3E%3C%2Fscript%3E%3Ctable%20width%3D%22200%22%20height%3D%2290%22%20align%3D%22center%22%20border%3D%220%22%3E%3Ctr%3E%3Ctd%20class%3D%22txt%22%3E%3Ccenter%3E%3Cform%20name%3D%22LoginForm%22%20action%3D%22%22%3E%3Ctable%20border%3D%220%22%20align%3D%22center%22%20width%3D%22100%25%22%3E%3Ctr%3E%3Ctd%20class%3D%22txt%22%3ELogin%3A%3C%2Ftd%3E%3Ctd%20class%3D%22txt%22%3E%3Cinput%20type%3D%22text%22%20name%3D%22login%22%20size%3D%2220%22%3E%3C%2Ftd%3E%3C%2Ftr%3E%3Ctr%3E%3Ctd%20class%3D%22txt%22%3EPassword%3A%3C%2Ftd%3E%3Ctd%20class%3D%22txt%22%3E%3Cinput%20type%3D%22password%22%20name%3D%22password%22%20size%3D%2220%22%3E%3C%2Ftd%3E%3C%2Ftr%3E%3C%2Ftable%3E%3Cinput%20type%3D%22submit%22%20value%3D%22Submit%22%20onClick%3D%22return%20validate%28%29%3B%22%3E%3C%2Fform%3E%3C%2Fcenter%3E%3C%2Ftd%3E%3C%2Ftr%3E%3C%2Ftable%3E%3C%2Fbody%3E%3C%2Fhtml%3E%0D%0A")
print(pwdok)
print("======== END OF passwordok ============")
print("Username is the word that results in the sha1 hash 1d31d94f30d40df7951505d1034e1e923d02ec49")
print("Password is the word that results in the sha1 hash 2d7a34c9ef8efa2cfdf4b89175f7edec1cd0ddda")
