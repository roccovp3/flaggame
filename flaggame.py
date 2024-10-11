from tkinter import *
import random
window = Tk()
window.title("Country Flags Game")
window.geometry("300x300")
randflag = random.randint(0, 195)
streak = 0
highscore = 0
flagimg = PhotoImage(file="country-flags/np.png")
flaglabel = Label(window, image=flagimg)
flaglabel.grid(row=2, column=0, pady=10)

def checkanswer(event):
    global highscore
    global randflag
    global streak
    global streaklabel
    guess = guessbox.get()
    streak = streak + 1
    if guess.lower() == answer.lower():
        label.config(text="Correct!\n ")
        displayupdate()
    elif guess.lower() == "Chad".lower():
        if randflag == 145:
            label.config(text="Correct!\n ")
            displayupdate()
    elif guess.lower() == "Romania".lower():
        if randflag == 167:
            label.config(text="Correct!\n ")
            displayupdate()
    elif guess.lower() == "Indonesia".lower():
        if randflag == 109:
            label.config(text="Correct!\n ")
            displayupdate()
    elif guess.lower() == "Monaco".lower():
        if randflag == 76:
            label.config(text="Correct!\n ")
            displayupdate()
    else:
        label.config(text=("Incorrect! The answer was\n" + listname[randflag]))
        displayupdate()
        streak = 0
    if streak >= 3:
        streaklabel = Label(text=(str(streak) + " in a row!"))
        streaklabel.grid(row=4, column=0)
    else:
        streaklabel = Label(text="                           ")
        streaklabel.grid(row=4, column=0)
    if streak > highscore:
        highscore = streak
    guessbox.delete(0, "end")


listname = [
 'Andorra', 'United Arab Emirates', 'Afghanistan', 'Antigua and Barbuda', 'Albania',
 'Armenia', 'Angola', 'Argentina', 'Austria', 'Australia', 'Azerbaijan',
 'Bosnia and Herzegovina', 'Barbados', 'Bangladesh', 'Belgium', 'Burkina Faso',
 'Bulgaria', 'Bahrain', 'Burundi', 'Benin', 'Brunei', 'Bolivia', 'Brazil',
 'Bahamas', 'Bhutan', 'Botswana', 'Belarus', 'Belize', 'Canada', 'Democratic Republic of the Congo',
 'Central African Republic', 'Republic of the Congo', 'Switzerland', 'Ivory Coast',
 'Chile', 'Cameroon', 'China', 'Colombia', 'Costa Rica', 'Cuba', 'Cape Verde',
 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Denmark', 'Dominica', 'Dominican Republic',
 'Algeria', 'Ecuador', 'Estonia', 'Egypt', 'Eritrea', 'Spain', 'Ethiopia',
 'Finland', 'Fiji', 'Micronesia', 'France', 'Gabon', 'United Kingdom', 'Grenada',
 'Georgia', 'French Guiana', 'Ghana', 'Gambia', 'Guinea', 'Equatorial Guinea',
 'Greece', 'Guatemala', 'Guinea-Bissau', 'Guyana', 'Honduras', 'Croatia',
 'Haiti', 'Hungary', 'Indonesia', 'Ireland', 'Israel', 'India', 'Iraq',
 'Iran', 'Iceland', 'Italy', 'Jamaica', 'Jordan', 'Japan', 'Kenya', 'Kyrgyzstan',
 'Cambodia', 'Comoros', 'Saint Kitts and Nevis', 'Kosovo', 'North Korea',
 'South Korea', 'Kuwait', 'Kazakhstan', 'Laos', 'Liberia', 'Saint Lucia',
 'Liechtenstein', 'Sri Lanka', 'Liberia', 'Lesotho', 'Lithuania', 'Luxembourg',
 'Latvia', 'Libya', 'Morocco', 'Monaco', 'Moldova', 'Montenegro', 'Madagascar',
 'Macedonia', 'Mali', 'Myanmar', 'Mongolia', 'Mauritania', 'Malta', 'Mauritius',
 'Maldives', 'Malawi', 'Mexico', 'Malaysia', 'Mozambique', 'Namibia', 'Niger',
 'Nigeria', 'Nicaragua', 'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand',
 'Oman', 'Panama', 'Peru', 'Papua New Guinea', 'Phillipines', 'Pakistan',
 'Poland', 'Portugal', 'Palau', 'Paraguay', 'Qatar', 'Romania', 'Serbia',
 'Russia', 'Rwanda', 'Saudi Arabia', 'Solomon Islands', 'Seychelles', 'Sudan',
 'Sweden', 'Singapore', 'Slovenia', 'Slovakia', 'Sierra Leone', 'San Marino',
 'Senegal', 'Somalia', 'Suriname', 'South Sudan', 'Sao Tome and Principe',
 'El Salvador', 'Syria', 'Swaziland', 'Chad', 'Togo', 'Thailand', 'Tajikistan',
 'East Timor', 'Turkmenistan', 'Tunisia', 'Tonga', 'Turkey', 'Trinidad and Tobago',
 'Tuvalu', 'Taiwan', 'Tanzania', 'Ukraine', 'Uganda', 'United States', 'Uruguay',
 'Uzbekistan', 'Vatican City', 'Saint Vincent and the Grenadines', 'Venezuela',
 'Vietnam', 'Vanuatu', 'Samoa', 'Yemen', 'South Africa', 'Zambia', 'Zimbabwe',
 'Marshall Islands']
listflag = ['ad.png', 'ae.png', 'af.png', 'ag.png', 'al.png', 'am.png', 'ao.png', 'ar.png',
 'at.png', 'au.png', 'az.png', 'ba.png', 'bb.png', 'bd.png', 'be.png', 'bf.png',
 'bg.png', 'bh.png', 'bi.png', 'bj.png', 'bn.png', 'bo.png', 'br.png', 'bs.png',
 'bt.png', 'bw.png', 'by.png', 'bz.png', 'ca.png', 'cd.png', 'cf.png', 'cg.png',
 'ch.png', 'ci.png', 'cl.png', 'cm.png', 'cn.png', 'co.png', 'cr.png', 'cu.png',
 'cv.png', 'cy.png', 'cz.png', 'de.png', 'dj.png', 'dk.png', 'dm.png', 'do.png',
 'dz.png', 'ec.png', 'ee.png', 'eg.png', 'er.png', 'es.png', 'et.png', 'fi.png',
 'fj.png', 'fm.png', 'fr.png', 'ga.png', 'gb.png', 'gd.png', 'ge.png', 'gf.png',
 'gh.png', 'gm.png', 'gn.png', 'gq.png', 'gr.png', 'gt.png', 'gw.png', 'gy.png',
 'hn.png', 'hr.png', 'ht.png', 'hu.png', 'id.png', 'ie.png', 'il.png', 'in.png',
 'iq.png', 'ir.png', 'is.png', 'it.png', 'jm.png', 'jo.png', 'jp.png', 'ke.png',
 'kg.png', 'kh.png', 'km.png', 'kn.png', 'kosovo.png', 'kp.png', 'kr.png',
 'kw.png', 'kz.png', 'la.png', 'lb.png', 'lc.png', 'li.png', 'lk.png', 'lr.png',
 'ls.png', 'lt.png', 'lu.png', 'lv.png', 'ly.png', 'ma.png', 'id.png', 'md.png',
 'me.png', 'mg.png', 'mk.png', 'ml.png', 'mm.png', 'mn.png', 'mr.png', 'mt.png',
 'mu.png', 'mv.png', 'mw.png', 'mx.png', 'my.png', 'mz.png', 'na.png', 'ne.png',
 'ng.png', 'ni.png', 'nl.png', 'no.png', 'np.png', 'nr.png', 'nz.png', 'om.png',
 'pa.png', 'pe.png', 'pg.png', 'ph.png', 'pk.png', 'pl.png', 'pt.png', 'pw.png',
 'py.png', 'qa.png', 'ro.png', 'rs.png', 'ru.png', 'rw.png', 'sa.png', 'sb.png',  'sc.png',
 'sd.png', 'se.png', 'sg.png', 'si.png', 'sk.png', 'sl.png', 'sm.png', 'sn.png',
 'so.png', 'sr.png', 'ss.png', 'st.png', 'sv.png', 'sy.png', 'sz.png', 'ro.png',
 'tg.png', 'th.png', 'tj.png', 'tl.png', 'tm.png', 'tn.png', 'to.png', 'tr.png',
 'tt.png', 'tv.png', 'tw.png', 'tz.png', 'ua.png', 'ug.png', 'us.png', 'uy.png',
 'uz.png', 'va.png', 'vc.png', 've.png', 'vn.png', 'vu.png', 'ws.png', 'ye.png',
 'za.png', 'zm.png', 'zw.png', 'mh.png']

def displayupdate():
    global answer
    global displayflag
    global flagimg
    global flaglabel
    global randflag
    randflag = random.randint(0, 195)
    displayflag = listflag[randflag]
    flagimg = PhotoImage(file=("country-flags/" + displayflag))
    flaglabel = Label(window, image=flagimg)
    flaglabel.grid(row=2, column=0, pady=10)
    answer = listname[randflag]
    highscorelabel = Label(text=("Highscore: " + str(highscore)))
    highscorelabel.grid(row=5, column=0)


displayupdate()
label = Label(text="What country's flag is this?\n ")
label.grid(row=0, column=0)
guessbox = Entry(window)
guessbox.grid(row=1, column=0)
window.bind("<Return>", checkanswer)
footer = Label(text="'The' is ommitted if it is the beginning\nof a countries name.\nCreated by Rocco Perciavalle. Updated October 21, 2017")
footer.grid(row=6, column=0)
mainloop()