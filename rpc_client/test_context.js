// Step up our game!
// Let's create some products in the DB

const DB = "psbe-custom"; // Replace with your DB name
const URL = "http://localhost:8069/jsonrpc"; // Replace with your URL
const PASS = "admin"; // Replace with your password
const UID = "2"; // Replace with your UID

const auctionListItalian = [
  ["_ext_id_.auction_tv", "TV"],
  ["_ext_id_.auction_car", "Macchina"],
  ["_ext_id_.auction_house", "Casa"],
  ["_ext_id_.auction_boat", "Barca"],
];

async function main() {
  const payload = {
    jsonrpc: "2.0", // Specify JSON-RPC version
    method: "call",
    params: {
      service: "object",
      method: "execute_kw",
      args: [
        DB,
        UID,
        PASS,
        "product.template",
        "load",
        [["id", "name"], auctionListItalian],
        {
          context: { lang: "it_IT" }, // Context for Italian translations
        },
      ],
    },
    id: 123, // This uniquely identifies the request
  };

  try {
    const response = await fetch(URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("Error:", error);
  }
}

main();
