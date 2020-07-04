mkdir -p ~/.streamlit/

echo "[general]\nemail = \"johnprimavesi@gmail.com\""  > ~/.streamlit/credentials.toml

echo "[server]\nheadless = true\nenableCORS = false\nport = $PORT" > ~/.streamlit/config.toml


