import streamlit as st


if 'cart_list' not in st.session_state:
    st.session_state.cart_list = [] 

products = ["Smartphone", "Laptop", "Headphone", "T-Shirt", "Jeans", "Jacket", "Rice", "Dal", "Oil"]
prices = [15000, 45000, 1200, 499, 999, 1500, 60, 110, 150]

def get_price(item):
    idx = products.index(item)
    return prices[idx]


def add_to_cart(item, qty):
    price = get_price(item)
    for i in range(len(st.session_state.cart_list)):
        if st.session_state.cart_list[i][0] == item:
            st.session_state.cart_list[i][2] += qty
            return
    st.session_state.cart_list.append([item, price, qty])


def update_quantity(item_name, new_qty):
    for i in range(len(st.session_state.cart_list)):
        if st.session_state.cart_list[i][0] == item_name:
            st.session_state.cart_list[i][2] = new_qty
            break


def remove_from_cart(item_name):
    for item in st.session_state.cart_list:
        if item[0] == item_name:
            st.session_state.cart_list.remove(item)
            break


st.set_page_config(page_title="Sourav's Mart", layout="wide")
st.title("🛒 Sourav's Mega Mart (Web Version)")
st.markdown("---")

col1, col2 = st.columns(2)


with col1:
    st.header("🛍️ Add Products")
    selected = st.selectbox("Select Product:", products)
    st.write(f"**Price:** ₹{get_price(selected)}")
    qty = st.number_input("Quantity:", min_value=1, value=1)
    
    if st.button("➕ Add to Cart", type="primary"):
        add_to_cart(selected, qty)
        st.success(f"✅ {selected} added to cart!")


with col2:
    st.header("🛒 Your Cart")
    if len(st.session_state.cart_list) == 0:
        st.info("Your cart is empty. Start shopping!")
    else:
        total = 0
        for i, item in enumerate(st.session_state.cart_list):
            item_name = item[0]
            item_price = item[1]
            item_qty = item[2]
            
            st.write(f"### {item_name}")
            st.write(f"Price: ₹{item_price} | Total: ₹{item_price * item_qty}")
            total += item_price * item_qty
            
            
            btn_col1, btn_col2 = st.columns(2)
            
            with btn_col1:
                new_q = st.number_input(f"Update Qty", min_value=1, value=item_qty, key=f"qty_{i}")
                if st.button(f"🔄 Update", key=f"upd_{i}"):
                    update_quantity(item_name, new_q)
                    st.rerun()
                    
            with btn_col2:
                st.write("") 
                st.write("")
                if st.button(f"❌ Remove", key=f"del_{i}"):
                    remove_from_cart(item_name)
                    st.rerun()
            
            st.markdown("---")
        
        st.subheader(f"Total Amount to Pay: ₹{total}")
        
        if st.button("💳 Checkout & Pay"):
            st.balloons()
            st.success("🎉 Payment Successful! Thank you for shopping.")
            st.session_state.cart_list.clear()
            st.rerun()