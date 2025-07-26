// src/components/UserInput.jsx
import React, { useState } from "react";
import { useChat } from "../context/ChatContext";
import axios from "axios";

const UserInput = () => {
  const [input, setInput] = useState("");
  const { addMessage } = useChat();

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMsg = { sender: "User", text: input };
    addMessage(userMsg);
    setInput("");

    try {
      const response = await axios.post("http://localhost:8000/api/chat", {
        message: input,
      });
      const botMsg = { sender: "Bot", text: response.data.response };
      addMessage(botMsg);
    } catch (error) {
      console.error("Error sending message:", error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex p-2 border-t">
      <input
        className="flex-1 border p-2 rounded mr-2"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type your message..."
      />
      <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">
        Send
      </button>
    </form>
  );
};

export default UserInput;

