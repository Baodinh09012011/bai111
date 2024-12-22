import streamlit as s

u = ('tra sua','tra chanh','tra tac')
d = ('duong den','duong trang')
t = ('tran chau','pudding','thach dua')

with s.form(key = 'dat do uong'):
  douong = s.selectbox('chon do uong',u)
  duong = s.selectbox('chon loai duong',d)
  thach = s.selectbox('chon loai thach',t)
  sl = s.slider('chon so luong',0,10,1)
  submit = s.form_submit_button('dat do uong')
  if submit:
    s.toast(f'ban da dat {sl} {douong} {duong} {thach}')

hd = {'loai do uong-':douong,'loai duong-':duong,'loai thach-':thach,'so luong-':sl}
hoadon = ''
for i in hd:
  hoadon += i + ' : ' + str(hd[i]) + '\n'

a = s.checkbox('in hoa don')
if a:
  s.download_button('in hoa don',hoadon,'hoadon.txt')
