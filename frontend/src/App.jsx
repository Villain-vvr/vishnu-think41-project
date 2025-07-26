import React from "react";
import ChatWindow from "./components/chatwindow";
import Sidebar from "./components/Sidebar";
import { ChatProvider } from "./context/ChatContext";

function App() {
  console.log("✅ App component rendered");

  return (
    <ChatProvider>
      <div className="flex h-screen">
        <Sidebar />
        <ChatWindow />
      </div>
    </ChatProvider>
  );
}

export default App;











