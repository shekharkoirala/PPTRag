import { useState, useEffect, useRef } from "react";
import axios from "axios";

const API_URL = "http://127.0.0.1:8000/search"; // Update with your API URL

function App() {
  const [query, setQuery] = useState("");
  const [messages, setMessages] = useState([]); // Stores conversation history
  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendQuery = async () => {
    if (!query) return;

    const newMessage = { role: "user", text: query, images: [] };
    setMessages((prev) => [...prev, newMessage]);
    setQuery("");
    setLoading(true);

    try {
      const res = await axios.post(API_URL, { query });
      const botResponse = {
        role: "bot",
        text: res.data.results,
        images: res.data.images || [],
      };

      setMessages((prev) => [...prev, botResponse]);
    } catch (error) {
      console.error("Error fetching response:", error);
    }

    setLoading(false);
  };

  return (
    <div className="bg-gray-900 min-h-screen flex flex-col items-center text-white">
      
      {/* Chat Header */}
      <header className="w-full max-w-4xl p-4 text-center text-2xl font-bold bg-gray-800">
        💬 RAG Chatbot
      </header>

      {/* Chat Messages */}
      <div className="flex-1 w-full max-w-4xl overflow-y-auto p-6 bg-gray-800 rounded-lg shadow-md h-[75vh]">
        {messages.map((msg, idx) => (
          <div key={idx} className={`mb-4 ${msg.role === "user" ? "text-right" : "text-left"}`}>
            <div className={`inline-block p-3 rounded-lg ${msg.role === "user" ? "bg-blue-600" : "bg-gray-700"}`}>
              {msg.text}
            </div>

            {/* Display Images */}
            {msg.images.length > 0 && (
              <div className="mt-2 grid grid-cols-2 gap-2">
                {msg.images.map((img, i) => (
                  <img key={i} src={`data:image/png;base64,${img}`} alt="Retrieved" className="w-40 rounded shadow" />
                ))}
              </div>
            )}
          </div>
        ))}
        <div ref={chatEndRef} />
      </div>

      {/* Chat Input at Bottom */}
      <div className="w-full max-w-4xl p-4 bg-gray-800 fixed bottom-0 flex items-center">
        <input
          type="text"
          className="flex-1 p-3 rounded bg-gray-700 text-white border-none outline-none"
          placeholder="Ask something..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyPress={(e) => e.key === "Enter" && sendQuery()}
        />
        <button className="ml-2 p-3 bg-blue-600 hover:bg-blue-700 rounded" onClick={sendQuery} disabled={loading}>
          {loading ? "⏳" : "Send"}
        </button>
      </div>
    </div>
  );
}

export default App;
