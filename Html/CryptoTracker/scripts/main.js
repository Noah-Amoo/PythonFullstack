const url =
  "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=8&page=1&sparkline=false";

const loadMarkets = async () => {
  try {
    const response = await fetch(url);
    const coins = await response.json();
    // console.log(coins);

    //Displays all fetched coins in the table on the markets page
    const tbody = document.querySelector("tbody");
    tbody.innerHTML = "";

    coins.forEach((coin) => {
      const row = document.createElement("tr");

      row.innerHTML = `
        <td>${coin.market_cap_rank}</td>
        <td>
            <img src="${coin.image}" alt="${coin.name} logo" width="20" height="20" />
            ${coin.name}
        </td>
        <td>${coin.current_price.toString()}</td>
        <td style="color: ${coin.price_change_percentage_24h >= 0 ? "lime" : "red"}>
            ${coin.price_change_percentage_24h.toFixed(2)}%
        </td>
        <td>$${coin.market_cap_rank.toString()}</td>
        <td>$${coin.total_volume.toString()}</td>
      `;

      row.style.cursor = "pointer";

      row.addEventListener("click", () => {
        window.location.href = `coin.html?${coin.id}`;
      });

      tbody.appendChild(row);
    });
  } catch (error) {
    console.error(error);
  }
};

loadMarkets();

// Defining the function to get coin details
const params = new URLSearchParams(window.location.search);
const coinId = params.get("id");

const loadCoinDetails = async () => {
  try {
    const response = await fetch(
      `https://api.coingecko.com/api/v3/coins/${coinId}`,
    );
    const coin = await response.json();

    const coinContent = document.querySelector("#coincontent");

    coinContent.style.color = "white"

    coinContent.innerHTML = `
            <h1>${coin.name}</h1>
            <img src="${coin.image.large}" alter="${coin.name} logo" width="80" height="80" />
            <p>Rank: ${coin.market_cap_rank}</p>
            <p>Price: $${coin.market_data.current_price.usd.toString()}
            <p>Market Cap: $${coin.market_data.market_cap.usd.toString()}
        `;
  } catch (error) {
    console.error(error);
  }
};

loadCoinDetails();
