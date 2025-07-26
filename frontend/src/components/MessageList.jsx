// src/components/MessageList.jsx
import React from "react";

const MessageList = ({ messages }) => {
  return (
    <div>
      {messages.length === 0 ? (
        <p className="text-gray-500">No messages yet</p>
      ) : (
        messages.map((msg, index) => (
          <div key={index} className="mb-2">
            <strong>{msg.sender}:</strong> {msg.text}
          </div>
        ))
      )}
    </div>
  );
};

export default MessageList;

