

def start1(request):
    pw_incorrect = False

    if request.session.get('is_authenticated', '') != '':
        if request.session.get('mode', '') == 'setup':
            return redirect('setup-mode/')
        elif request.session.get('mode', '') == 'operative':
            return redirect('operative-mode/')

    if request.method == 'POST':

        if fct.verify_pw(request.POST['email'], request.POST['pw']):
            request.session['is_authenticated'] = request.POST['email']
            request.session['mode'] = fct.user_mode(request.POST['email'])

            if fct.user_mode(request.POST['email']) == 'setup':
                return redirect('setup-mode/')
            elif fct.user_mode(request.POST['email']) == 'operative':
                return redirect('operative-mode/')

        else:
            request.session['is_authenticated'] = ''
            pw_incorrect = True
    
    return render(request, 'login.html', {'pw_incorrect': pw_incorrect})



def create_user(mode, firstname, lastname, street, postalcode, city, email, pw):

    hashed = bcrypt.hashpw(bytes(pw, 'utf-8'), bcrypt.gensalt())

    hashed = str(hashed, 'utf-8')

    User.objects.create(mode=mode,
    user_id=get_companyID(),
    company_id=0,
    firstname=firstname,
    lastname=lastname,
    street=street,
    postalcode=postalcode,
    city=city,
    email=email,
    pw=hashed)


    
