import streamlit as st
import pickle


products = pickle.load(open(r"C:\Users\kelvin leung\Desktop\product_list.f.pkl", 'rb'))
similarity = pickle.load(open(r"C:\Users\kelvin leung\Desktop\similarity.f.pkl", 'rb'))
photos = pickle.load(open(r"C:\Users\kelvin leung\Desktop\url.f.pkl", 'rb'))
product_price = pickle.load(open(r"C:\Users\kelvin leung\Desktop\price.p.pkl", 'rb'))


st.header("Product Recommendation System")

products_list = products['product_name'].values

selectvalue = st.selectbox("Select product", products_list)





def recommend(product):
    index=products[products['product_name']==product].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_product=[]
    photos_url =[]
    prices = []
    for i in distance[1:6]:
        recommend_product.append(products.iloc[i[0]].product_name)  
        photos_url.append(photos.iloc[i[0]].product_image_url)
        prices.append(product_price.iloc[i[0]].price)
    return recommend_product, photos_url, prices






if st.button("Show Recommend"):
    products_name, products_photo, selling_price = recommend(selectvalue)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(products_name[0])
        st.image(products_photo[0])
        st.text("₹")
        st.text(selling_price[0])
    with col2:
        st.text(products_name[1])
        st.image(products_photo[1])
        st.text("₹")
        st.text(selling_price[1])
    with col3:
        st.text(products_name[2])
        st.image(products_photo[2])
        st.text("₹")
        st.text(selling_price[2])
    with col4:
        st.text(products_name[3]) 
        st.image(products_photo[3])
        st.text("₹")
        st.text(selling_price[3])
    with col5:
        st.text(products_name[4])
        st.image(products_photo[4])
        st.text("₹")
        st.text(selling_price[4])