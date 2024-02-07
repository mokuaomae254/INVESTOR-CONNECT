
import streamlit as st

network_payment_options = {
    'BNB CHAIN': ['BUSD'],
    'SOLANA': ['USDC', 'USDT'],
    'BASE': ['USDBC'],
    'POLYGON': ['USDC', 'DAI', 'USDT'],
    'OPTIMISM': ['USDC'],
    'AVALANCHE': ['USDC'],
    'ETHEREUM': ['USDC']  # Add options for ETHEREUM
}

st.write('Donate to support our development')

network_options = list(network_payment_options.keys())

selected_network = st.selectbox('Choose a network:', network_options)

st.write(f'You selected network: {selected_network}')

payment_options = network_payment_options.get(selected_network, [])

if payment_options:
    selected_payment_option = st.selectbox('Choose a payment option:', payment_options)
    st.write(f'You selected payment option: {selected_payment_option}')
    
    # Set receiver address based on the selected network
    if selected_network == 'SOLANA':
        receiver_address = "9N2RjpW6kUdQL9ooU8dobhBeuGjLVVTfjUVmGp1uoghm"
    else:
        receiver_address = "0x1560fE2D29b86a0B0040e96545bDe4531E3feBD3"
    
    # Generate HTML code for the selected payment option
    html_code = f"""
    <script src="https://button.getpip.com/cdn/pipbutton.js"></script>
    <div class="pip-button"
         data-amount="10"
         data-chainNetwork="{selected_network}"
         data-currency="{selected_payment_option}"
         data-label="PAY"
         data-useLabel="true"
         data-receiver="{receiver_address}"
         data-buttonColor="#1149FF"
         data-buttonTextColor="#FFFFFF"
         data-memo="{receiver_address}">
    </div>
    """

    st.components.v1.html(html_code, height=600, width=400)
    
else:
    st.write('No payment options available for the selected network.')

st.write('Thank you for your donation')


#streamlit run crypto_donations.py
