const Message = ({ role, text }) => {
  const isUser = role === "user";
  return (
    <div
      className={`p-2 rounded-xl max-w-xs ${
        isUser ? "bg-blue-200 self-end text-right" : "bg-white self-start"
      }`}
    >
      <p>{text}</p>
    </div>
  );
};

export default Message;
