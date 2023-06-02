import streamlit as st

def main():
    st.title("Stock Market Trading And Trend Apps")
    st.markdown('<h1 style="color:blue;">Invest In Groww</h1>', unsafe_allow_html=True)

    paragraph = "Groww is a great platform for investment. Interactive and clean User Interface. Features like creating your own portfolio are great..I started investing in MF due to Groww only. Very responsive Support team. Always available to help for any query"
    st.write(paragraph)
    st.markdown('<h2 style="color:green;">Stock Invest In Grow</h2>', unsafe_allow_html=True)

    video_url = "https://www.youtube.com/watch?v=a_hxQZTaXKI"
    st.video(video_url, start_time=0)

    image_url = "https://assets-netstorage.groww.in/web-assets/nbg_mobile/prod/_next/static/media/demat-hero-img.60f65216.png"
    st.image(image_url, caption='Sample Image')
    
    st.markdown('[Groww Link](https://www.groww.in)')


    
    st.markdown('<h1 style="color:blue;">Invest In Upstox</h1>', unsafe_allow_html=True)

    paragraph = "However, you can easily open an Upstox free Demat account online, without any opening charges or account maintenance charges. This best demat account is more than just a depository for investors' securities. It is a move to bring transparency and regulation to the securities markets."

    st.write(paragraph)
    st.markdown('<h2 style="color:green;">Stock Invest In Upstox</h2>', unsafe_allow_html=True)

    video_url = "https://youtu.be/91OGyKQy51Y"
    st.video(video_url, start_time=0)

    image_url = "https://www.newsexperts.in/wp-content/uploads/2021/01/upstox-1280x720.jpg"
    st.image(image_url, caption='Sample Image')
    
    st.markdown('[Upstox Link](https://www.upstox.in)')


    st.markdown('<h1 style="color:blue;">Invest In Zerodha</h1>', unsafe_allow_html=True)

    paragraph = "Super thrilled to announce the launch of Kite 3.0 beta. It has taken our technology team one whole year to rebuild the vast Kite ecosystem from the ground up, all the way from the backend systems, APIs, and to the web front-end. We have learnt and adopted new technologies and have replaced the underlying ones completely. Kite 3.0 significantly improves on performance, design and UX, and comes with a host of new features."

    st.write(paragraph)
    st.markdown('<h2 style="color:green;">Stock Invest In Zerodha</h2>', unsafe_allow_html=True)

    video_url = "https://youtu.be/Je8dWUZRx_E"
    st.video(video_url, start_time=0)

    image_url = "https://zerodha.com/z-connect/wp-content/uploads/2017/12/MarketwatchSettings-1024x730.png"
    st.image(image_url, caption='Sample Image')
    
    st.markdown('[Zerodha Link](https://www.kite.zerodha.com)')


    st.markdown('<h1 style="color:blue;">Invest In Angel Broking</h1>', unsafe_allow_html=True)

    paragraph = "To avail lucrative returns on your investments, Angel One empowers you with the knowledge of stock trading and investment. Our knowledge bank is divided into different modules that explain related investment concepts, terms, strategies, and practices, such that you will be able to trade in the market in a better manner."

    st.write(paragraph)
    st.markdown('<h2 style="color:green;">Stock Invest In Angel Broking</h2>', unsafe_allow_html=True)

    video_url = "https://youtu.be/_B7bUuOu5DQ"
    st.video(video_url, start_time=0)

    image_url = "https://w3assets.angelone.in/wp-content/uploads/2022/01/access-charts-angelone.png"
    st.image(image_url, caption='Sample Image')
    
    st.markdown('[Angel Broking Link](https://www.angelone.in)')



if __name__ == "__main__":
    main()


    st.title("Stock Market Basics - Important Terms")

    terms = [
        ("Sensex", "Sensex is a collection of the top 30 stocks listed on BSE by way of market capitalisation."),
        ("SEBI", "Securities and Exchange Board of India (SEBI) is the securities market regulator to oversee any fraudulent transactions and activities made by any of the parties: companies, investors, traders, brokers and the likes."),
        ("Demat", "Demat, or dematerialised account, is a form of an online portfolio that holds a customer’s shares and other securities in an electronic (dematerialised) format."),
        ("Trading", "It is the process of buying or selling of shares in a company."),
        ("Stock Index", "A stock index or stock market index is a statistical source that measures financial market fluctuations. They are performance indicators that indicate the performance of a certain market segment or the market as a whole."),
        ("Portfolio", "It is a collection of a wide range of assets that are owned by investors. Portfolio can also include valuables ranging from gold, stocks, funds, derivatives, property, cash equivalents, bonds, etc."),
        ("Bull Market", "In a bull market, companies tend to generate more revenue, and as the economy grows, consumers are more likely to spend."),
        ("Bear Market", "Bear markets refers to a slowdown in the economy, which may make consumers less likely to spend and, in turn, lower the GDP."),
        ("Nifty50", "Nifty 50 is a collection of the top 50 companies listed on National Stock Exchange (NSE)."),
        ("Stock Market Broker", "A stock broker is an investment advisor who execute transactions such as the buying and selling of stocks on behalf of their clients."),
        ("Bid Price", "Bid price is the highest price a buyer will pay to buy a specified number of shares of a stock at any given time."),
        ("Ask Price", "Ask price in stock market refers to the lowest price at which a seller will sell the stock."),
        ("IPO", "Initial Public Offer (IPO) is the selling of securities to the public in the primary market. It is the largest source of funds with long or indefinite maturity for the company."),
        ("Equity", "Equity is the value that would be received by the shareholder if all of the company’s assets were liquidated and all of the company's debts were paid off."),
        ("Dividend", "Dividend refers to cash or reward that a company provides to its shareholders. It can be issued in various forms, such as cash payment, stocks or any other form."),
        ("BSE", "Bombay Stock Exchange (BSE) is the largest and first securities exchange market in India. It was established in 1875 as the Native Share and Stock Brokers' Association. It is also the first stock exchange in India and provides an equities trading platform for small-and-medium enterprises."),
        ("NSE", "National Stock Exchange was the first to implement screen-based or electronic trading in India. It is the fourth largest stock exchange in the world in terms of equity trading volume as per the World Federation of Exchanges (WFE)."),
        ("Call & Put Option", "Call option give the investor the right to purchase the underlying security, while put option give the investor the right to sell shares of the underlying security. Both the option let the investors profit from movements in a stock's price."),
        # Add more terms here...
    ]

    for term, definition in terms:
        st.write(f"**{term}:**")
        st.write(definition)
        st.write("") 

    

