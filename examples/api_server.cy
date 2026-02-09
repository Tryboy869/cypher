# API REST Server
A(get_users)
G(get_users;endpoint:/api/users;method:GET)
C(get_users;database)
T(get_users;format:json)
F(get_users;fixed)

A(create_user)
G(create_user;endpoint:/api/users;method:POST)
T(create_user;validate:email)
I(create_user;valid)
C(create_user;database)
G(create_user;query:INSERT INTO users)
T(create_user;return:201)
J(create_user;error)
T(create_user;return:400)
F(create_user;fixed)

L(api;life)
