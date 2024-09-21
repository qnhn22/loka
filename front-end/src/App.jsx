import {
  useLogoutFunction,
  useRedirectFunctions,
  withAuthInfo,
} from "@propelauth/react";
import Home from "./pages/Home";
import { Routes, Route } from "react-router-dom";
const App = withAuthInfo(({ isLoggedIn }) => {
  const logoutFn = useLogoutFunction();
  const { redirectToSignupPage, redirectToLoginPage } = useRedirectFunctions();
  const authedButtonList = [
    ["Sign up", () => redirectToSignupPage()],
    ["Log in", () => redirectToLoginPage()],
  ];
  const unAuthedButtonList = [["Log out", () => logoutFn()]];
  const Navbar = ({ buttons }) => {
    return (
      <nav className="bg-gray-800 p-4">
        <div className="container mx-auto flex justify-between items-center">
          <div className="text-white text-lg font-bold">Loka</div>
          <div className="flex space-x-4">
            {buttons.map(([name, action], index) => (
              <button
                key={index}
                className="text-white hover:text-gray-400"
                onClick={action}
              >
                {name}
              </button>
            ))}
          </div>
        </div>
      </nav>
    );
  };
  if (isLoggedIn) {
    return (
      <div>
        <Navbar buttons={unAuthedButtonList} />
        <Routes>
          <Route exact path="/" element={<Home />} />
          {/* <Route path="/user_info" element={<UserInfo/>}/> */}
        </Routes>
      </div>
    );
  } else {
    return (
      <div>
        <Navbar buttons={authedButtonList} />
        <div className="flex flex-col"></div>
        <div className="flex flex-col justify-center items-center h-screen bg-gray-50 ">
        <span className="text-5xl font-bold mb-6 mt-[-60px]">Loka</span>
          <span className="text-xl font-semibold text-gray-700">
            A novel solution to help you find the best locations for your
            restaurant.
          </span>
        </div>
      </div>
    );
  }
});
export default App;
