// src/components/ChatWindow.jsx
import React from "react";
import { useChat } from "../context/ChatContext";
import MessageList from "./MessageList";
import UserInput from "./UserInput";
import SidePanel from "./SidePanel";

const ChatWindow = () => {
  const { messages } = useChat();

  return (
    <div className="flex-1 flex flex-col bg-white">
      <div className="flex-1 overflow-auto p-4">
        <MessageList messages={messages} />
      </div>
      <UserInput />
    </div>
  );
};

export default ChatWindow;





