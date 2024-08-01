    NavigateToResource,
    UnsavedChangesNotifier,
} from "@refinedev/react-router-v6";
import { App as AntdApp } from "antd";
import axios from "axios";
import { Header } from "./components/Header";
import { ColorModeContextProvider } from "./contexts/color-mode";
import {
    ArticleList,
    ArticleCreate,
    ArticleEdit,
    ArticleShow,
} from "./pages/articles";
import { parseJwt } from "./utils/parse-jwt";
import dataProvider from "./providers/dataProvider";
import LoginPage, { action as loginAction } from "./routes/login";
const axiosInstance = axios.create();
axiosInstance.interceptors.request.use((config) => {
    const token = localStorage.getItem("token");
    if (config.headers) {
        config.headers["Authorization"] = `Bearer ${token}`;
    }
    return config;
});
function App() {     const authProvider: AuthBindings = {;         login: async ({ credential }) => {
            const profileObj = credential ? parseJwt(credential) : null;
            if (profileObj) {
                localStorage.setItem(
                    "user",
                    JSON.stringify({
                        ...profileObj,
                        avatar: profileObj.picture,
                    })
                );
                localStorage.setItem("token", `${credential}`);
                return {
                    success: true,
                    redirectTo: "/",
                };
            }
            return {
                success: false,
            };
        },
        logout: async () => {
            const token = localStorage.getItem("token");
            if (token && typeof window !== "undefined") {
                localStorage.removeItem("token");
                localStorage.removeItem("user");
                axios.defaults.headers.common = {};
                window.google?.accounts.id.revoke(token, () => {
                    return {};
                });
            }
            return {
                success: true,
                redirectTo: "/login",
            };
        },
        onError: async (error) => {
            console.error(error);
            return { error };
        },
        check: async () => {
            const token = localStorage.getItem("token");
            if (token) {
                return {
                    authenticated: true,
                };
            }
            return {
                authenticated: false,
                error: {
                    message: "Check failed",
                    name: "Token not found",
                },
                logout: true,
                redirectTo: "/login",
            };
        },
        getPermissions: async () => null,
        getIdentity: async () => {
            const user = localStorage.getItem("user");
            if (user) {
                return JSON.parse(user);
            }
            return null;
        },
    };
    return (
        <BrowserRouter>
            <GitHubBanner />
            <RefineKbarProvider>
                <ColorModeContextProvider>
                    <AntdApp>
                        <DevtoolsProvider>
                            <Refine
                                dataProvider={dataProvider}
                                notificationProvider={useNotificationProvider}
                                authProvider={authProvider}
                                resources={[
                                    {                                         name: "articles",;                                         list: "/articles",;                                         create: "/articles/create",;                                         edit: "/articles/edit/:id",;                                         show: "/articles/show/:id",;                                         meta: {;                                             canDelete: true,;                                         },;                                     },;                                 ]};                                 options={{;                                     syncWithLocation: true,;                                     warnWhenUnsavedChanges: true,;                                     useNewQueryKeys: true,;                                     projectId: "aD7zNw-fPk4Vm-0q43Xn",;                                 }};                             >
                                <Routes>
                                    <Route
                                        element={
                                            <Authenticated
                                                key="authenticated-inner"
                                                fallback={<CatchAllNavigate to="/login" />}
                                            >
                                                <ThemedLayoutV2
                                                    Header={Header}
                                                    Sider={(props) => (
                                                        <ThemedSiderV2 {...props} fixed />
                                                    )}
                                                >
                                                    <Outlet />
                                                </ThemedLayoutV2>
                                            </Authenticated>
                                        }
                                    >
                                        <Route
                                            index
                                            element={<NavigateToResource resource="articles" />}
                                        />
                                        <Route path="/articles">
                                            <Route index element={<ArticleList />} />
                                            <Route path="create" element={<ArticleCreate />} />
                                            <Route path="edit/:id" element={<ArticleEdit />} />
                                            <Route path="show/:id" element={<ArticleShow />} />
                                        </Route>
                                        <Route path="*" element={<ErrorComponent />} />
                                    </Route>
                                    <Route path="/login" element={<LoginPage />} />
                                </Routes>
                                <RefineKbar />
                                <UnsavedChangesNotifier />
                                <DocumentTitleHandler />
                            </Refine>
                            <DevtoolsPanel />
                        </DevtoolsProvider>
                    </AntdApp>
                </ColorModeContextProvider>
            </RefineKbarProvider>
        </BrowserRouter>
    );
}
export default App;
bash: syntax error near unexpected token `}'
npm run dev
npm install @tanstack/react-query
npm install @tanstack/react-query
npm run dev
SESSION_SECRET: "123456*a1"
@remix-run_node.js?v=a464a21f:26886 Module "stream" has been externalized for browser compatibility. Cannot access "stream.Transform" in client code. See http://vitejs.dev/guide/troubleshooting.html#module-externalized-for-browser-compatibility for more details.
get @ @remix-run_node.js?v=a464a21f:26886
../node_modules/stream-slice/index.js @ @remix-run_node.js?v=a464a21f:26897
__require2 @ chunk-7B76BHIQ.js?v=3f512e7b:19
../node_modules/@remix-run/node/dist/upload/fileUploadHandler.js @ @remix-run_node.js?v=a464a21f:27093
__require2 @ chunk-7B76BHIQ.js?v=3f512e7b:19
../node_modules/@remix-run/node/dist/index.js @ @remix-run_node.js?v=a464a21f:27281
__require2 @ chunk-7B76BHIQ.js?v=3f512e7b:19
(anonymous) @ @remix-run_node.js?v=a464a21f:27395
Show 8 more frames
Show lessUnderstand this warning
auth.ts:4 SESSION_SECRET: "123456*a1"
chunk-TV2X25GZ.js?v=3f512e7b:6125 Uncaught Error: No QueryClient set, use QueryClientProvider to set one
    at useQueryClient (chunk-TV2X25GZ.js?v=3f512e7b:6125:11)
    at useInvalidateAuthStore (chunk-TV2X25GZ.js?v=3f512e7b:8917:11)
    at useLogout (chunk-TV2X25GZ.js?v=3f512e7b:8923:11)
    at ThemedSiderV2 (@refinedev_antd.js?v=37a19b68:46067:553)
    at renderWithHooks (chunk-KAPPEO6M.js?v=3f512e7b:11568:26)
    at mountIndeterminateComponent (chunk-KAPPEO6M.js?v=3f512e7b:14946:21)
    at beginWork (chunk-KAPPEO6M.js?v=3f512e7b:15934:22)
    at HTMLUnknownElement.callCallback2 (chunk-KAPPEO6M.js?v=3f512e7b:3674:22)
    at Object.invokeGuardedCallbackDev (chunk-KAPPEO6M.js?v=3f512e7b:3699:24)
    at invokeGuardedCallback (chunk-KAPPEO6M.js?v=3f512e7b:3733:39)
useQueryClient @ chunk-TV2X25GZ.js?v=3f512e7b:6125
useInvalidateAuthStore @ chunk-TV2X25GZ.js?v=3f512e7b:8917
useLogout @ chunk-TV2X25GZ.js?v=3f512e7b:8923
ThemedSiderV2 @ @refinedev_antd.js?v=37a19b68:46067
renderWithHooks @ chunk-KAPPEO6M.js?v=3f512e7b:11568
mountIndeterminateComponent @ chunk-KAPPEO6M.js?v=3f512e7b:14946
beginWork @ chunk-KAPPEO6M.js?v=3f512e7b:15934
callCallback2 @ chunk-KAPPEO6M.js?v=3f512e7b:3674
invokeGuardedCallbackDev @ chunk-KAPPEO6M.js?v=3f512e7b:3699
invokeGuardedCallback @ chunk-KAPPEO6M.js?v=3f512e7b:3733
beginWork$1 @ chunk-KAPPEO6M.js?v=3f512e7b:19793
performUnitOfWork @ chunk-KAPPEO6M.js?v=3f512e7b:19226
workLoopSync @ chunk-KAPPEO6M.js?v=3f512e7b:19165
renderRootSync @ chunk-KAPPEO6M.js?v=3f512e7b:19144
performConcurrentWorkOnRoot @ chunk-KAPPEO6M.js?v=3f512e7b:18706
workLoop @ chunk-KAPPEO6M.js?v=3f512e7b:197
flushWork @ chunk-KAPPEO6M.js?v=3f512e7b:176
performWorkUntilDeadline @ chunk-KAPPEO6M.js?v=3f512e7b:384
Show 18 more frames
Show lessUnderstand this error
chunk-UYPYS5OR.js?v=3f512e7b:2425 Warning: [antd: Menu] `children` is deprecated. Please use `items` instead.
warning @ chunk-UYPYS5OR.js?v=3f512e7b:2425
call @ chunk-UYPYS5OR.js?v=3f512e7b:2444
warningOnce @ chunk-UYPYS5OR.js?v=3f512e7b:2449
warning2 @ chunk-UYPYS5OR.js?v=3f512e7b:5613
typeWarning @ chunk-UYPYS5OR.js?v=3f512e7b:5639
typeWarning.deprecated @ chunk-UYPYS5OR.js?v=3f512e7b:5644
(anonymous) @ chunk-UYPYS5OR.js?v=3f512e7b:34118
renderWithHooks @ chunk-KAPPEO6M.js?v=3f512e7b:11568
updateForwardRef @ chunk-KAPPEO6M.js?v=3f512e7b:14345
beginWork @ chunk-KAPPEO6M.js?v=3f512e7b:15966
beginWork$1 @ chunk-KAPPEO6M.js?v=3f512e7b:19781
performUnitOfWork @ chunk-KAPPEO6M.js?v=3f512e7b:19226
workLoopSync @ chunk-KAPPEO6M.js?v=3f512e7b:19165
renderRootSync @ chunk-KAPPEO6M.js?v=3f512e7b:19144
performConcurrentWorkOnRoot @ chunk-KAPPEO6M.js?v=3f512e7b:18706
workLoop @ chunk-KAPPEO6M.js?v=3f512e7b:197
flushWork @ chunk-KAPPEO6M.js?v=3f512e7b:176
performWorkUntilDeadline @ chunk-KAPPEO6M.js?v=3f512e7b:384
Show 18 more frames
Show lessUnderstand this error
chunk-TV2X25GZ.js?v=3f512e7b:6125 Uncaught Error: No QueryClient set, use QueryClientProvider to set one
    at useQueryClient (chunk-TV2X25GZ.js?v=3f512e7b:6125:11)
    at useInvalidateAuthStore (chunk-TV2X25GZ.js?v=3f512e7b:8917:11)
    at useLogout (chunk-TV2X25GZ.js?v=3f512e7b:8923:11)
    at useOnError (chunk-TV2X25GZ.js?v=3f512e7b:9015:156)
    at useList (chunk-TV2X25GZ.js?v=3f512e7b:9049:110)
    at useTable (chunk-TV2X25GZ.js?v=3f512e7b:9948:12)
    at ArticleList (ArticleList.tsx:8:28)
    at renderWithHooks (chunk-KAPPEO6M.js?v=3f512e7b:11568:26)
    at mountIndeterminateComponent (chunk-KAPPEO6M.js?v=3f512e7b:14946:21)
    at beginWork (chunk-KAPPEO6M.js?v=3f512e7b:15934:22)
useQueryClient @ chunk-TV2X25GZ.js?v=3f512e7b:6125
useInvalidateAuthStore @ chunk-TV2X25GZ.js?v=3f512e7b:8917
useLogout @ chunk-TV2X25GZ.js?v=3f512e7b:8923
useOnError @ chunk-TV2X25GZ.js?v=3f512e7b:9015
useList @ chunk-TV2X25GZ.js?v=3f512e7b:9049
useTable @ chunk-TV2X25GZ.js?v=3f512e7b:9948
ArticleList @ ArticleList.tsx:8
renderWithHooks @ chunk-KAPPEO6M.js?v=3f512e7b:11568
mountIndeterminateComponent @ chunk-KAPPEO6M.js?v=3f512e7b:14946
beginWork @ chunk-KAPPEO6M.js?v=3f512e7b:15934
callCallback2 @ chunk-KAPPEO6M.js?v=3f512e7b:3674
invokeGuardedCallbackDev @ chunk-KAPPEO6M.js?v=3f512e7b:3699
invokeGuardedCallback @ chunk-KAPPEO6M.js?v=3f512e7b:3733
beginWork$1 @ chunk-KAPPEO6M.js?v=3f512e7b:19793
performUnitOfWork @ chunk-KAPPEO6M.js?v=3f512e7b:19226
workLoopSync @ chunk-KAPPEO6M.js?v=3f512e7b:19165
renderRootSync @ chunk-KAPPEO6M.js?v=3f512e7b:19144
performConcurrentWorkOnRoot @ chunk-KAPPEO6M.js?v=3f512e7b:18706
workLoop @ chunk-KAPPEO6M.js?v=3f512e7b:197
flushWork @ chunk-KAPPEO6M.js?v=3f512e7b:176
performWorkUntilDeadline @ chunk-KAPPEO6M.js?v=3f512e7b:384
Show 20 more frames
Show lessUnderstand this error
chunk-TV2X25GZ.js?v=3f512e7b:6125 Uncaught Error: No QueryClient set, use QueryClientProvider to set one
    at useQueryClient (chunk-TV2X25GZ.js?v=3f512e7b:6125:11)
    at useInvalidateAuthStore (chunk-TV2X25GZ.js?v=3f512e7b:8917:11)
    at useLogout (chunk-TV2X25GZ.js?v=3f512e7b:8923:11)
    at ThemedSiderV2 (@refinedev_antd.js?v=37a19b68:46067:553)
    at renderWithHooks (chunk-KAPPEO6M.js?v=3f512e7b:11568:26)
    at mountIndeterminateComponent (chunk-KAPPEO6M.js?v=3f512e7b:14946:21)
    at beginWork (chunk-KAPPEO6M.js?v=3f512e7b:15934:22)
    at HTMLUnknownElement.callCallback2 (chunk-KAPPEO6M.js?v=3f512e7b:3674:22)
    at Object.invokeGuardedCallbackDev (chunk-KAPPEO6M.js?v=3f512e7b:3699:24)
    at invokeGuardedCallback (chunk-KAPPEO6M.js?v=3f512e7b:3733:39)
useQueryClient @ chunk-TV2X25GZ.js?v=3f512e7b:6125
useInvalidateAuthStore @ chunk-TV2X25GZ.js?v=3f512e7b:8917
useLogout @ chunk-TV2X25GZ.js?v=3f512e7b:8923
ThemedSiderV2 @ @refinedev_antd.js?v=37a19b68:46067
renderWithHooks @ chunk-KAPPEO6M.js?v=3f512e7b:11568
mountIndeterminateComponent @ chunk-KAPPEO6M.js?v=3f512e7b:14946
beginWork @ chunk-KAPPEO6M.js?v=3f512e7b:15934
callCallback2 @ chunk-KAPPEO6M.js?v=3f512e7b:3674
invokeGuardedCallbackDev @ chunk-KAPPEO6M.js?v=3f512e7b:3699
invokeGuardedCallback @ chunk-KAPPEO6M.js?v=3f512e7b:3733
beginWork$1 @ chunk-KAPPEO6M.js?v=3f512e7b:19793
performUnitOfWork @ chunk-KAPPEO6M.js?v=3f512e7b:19226
workLoopSync @ chunk-KAPPEO6M.js?v=3f512e7b:19165
renderRootSync @ chunk-KAPPEO6M.js?v=3f512e7b:19144
recoverFromConcurrentError @ chunk-KAPPEO6M.js?v=3f512e7b:18764
performConcurrentWorkOnRoot @ chunk-KAPPEO6M.js?v=3f512e7b:18712
workLoop @ chunk-KAPPEO6M.js?v=3f512e7b:197
flushWork @ chunk-KAPPEO6M.js?v=3f512e7b:176
performWorkUntilDeadline @ chunk-KAPPEO6M.js?v=3f512e7b:384
Show 19 more frames
Show lessUnderstand this error
chunk-TV2X25GZ.js?v=3f512e7b:6125 Uncaught Error: No QueryClient set, use QueryClientProvider to set one
    at useQueryClient (chunk-TV2X25GZ.js?v=3f512e7b:6125:11)
    at useInvalidateAuthStore (chunk-TV2X25GZ.js?v=3f512e7b:8917:11)
    at useLogout (chunk-TV2X25GZ.js?v=3f512e7b:8923:11)
    at useOnError (chunk-TV2X25GZ.js?v=3f512e7b:9015:156)
    at useList (chunk-TV2X25GZ.js?v=3f512e7b:9049:110)
    at useTable (chunk-TV2X25GZ.js?v=3f512e7b:9948:12)
    at ArticleList (ArticleList.tsx:8:28)
    at renderWithHooks (chunk-KAPPEO6M.js?v=3f512e7b:11568:26)
    at mountIndeterminateComponent (chunk-KAPPEO6M.js?v=3f512e7b:14946:21)
    at beginWork (chunk-KAPPEO6M.js?v=3f512e7b:15934:22)
useQueryClient @ chunk-TV2X25GZ.js?v=3f512e7b:6125
useInvalidateAuthStore @ chunk-TV2X25GZ.js?v=3f512e7b:8917
useLogout @ chunk-TV2X25GZ.js?v=3f512e7b:8923
useOnError @ chunk-TV2X25GZ.js?v=3f512e7b:9015
useList @ chunk-TV2X25GZ.js?v=3f512e7b:9049
useTable @ chunk-TV2X25GZ.js?v=3f512e7b:9948
ArticleList @ ArticleList.tsx:8
renderWithHooks @ chunk-KAPPEO6M.js?v=3f512e7b:11568
mountIndeterminateComponent @ chunk-KAPPEO6M.js?v=3f512e7b:14946
beginWork @ chunk-KAPPEO6M.js?v=3f512e7b:15934
callCallback2 @ chunk-KAPPEO6M.js?v=3f512e7b:3674
invokeGuardedCallbackDev @ chunk-KAPPEO6M.js?v=3f512e7b:3699
invokeGuardedCallback @ chunk-KAPPEO6M.js?v=3f512e7b:3733
beginWork$1 @ chunk-KAPPEO6M.js?v=3f512e7b:19793
performUnitOfWork @ chunk-KAPPEO6M.js?v=3f512e7b:19226
workLoopSync @ chunk-KAPPEO6M.js?v=3f512e7b:19165
renderRootSync @ chunk-KAPPEO6M.js?v=3f512e7b:19144
recoverFromConcurrentError @ chunk-KAPPEO6M.js?v=3f512e7b:18764
performConcurrentWorkOnRoot @ chunk-KAPPEO6M.js?v=3f512e7b:18712
workLoop @ chunk-KAPPEO6M.js?v=3f512e7b:197
flushWork @ chunk-KAPPEO6M.js?v=3f512e7b:176
performWorkUntilDeadline @ chunk-KAPPEO6M.js?v=3f512e7b:384
Show 21 more frames
Show lessUnderstand this error
chunk-KAPPEO6M.js?v=3f512e7b:14052 The above error occurred in the <ThemedSiderV2> component:
    at ThemedSiderV2 (http://localhost:5173/node_modules/.vite/deps/@refinedev_antd.js?v=37a19b68:46065:23)
    at Sider
    at div
    at http://localhost:5173/node_modules/.vite/deps/chunk-UYPYS5OR.js?v=3f512e7b:64217:16
    at Layout
    at ThemedLayoutContextProvider (http://localhost:5173/node_modules/.vite/deps/@refinedev_antd.js?v=37a19b68:45982:26)
    at ThemedLayoutV2 (http://localhost:5173/node_modules/.vite/deps/@refinedev_antd.js?v=37a19b68:46097:26)
    at RenderedRoute (http://localhost:5173/node_modules/.vite/deps/react-router-dom.js?v=1baeb357:4015:5)
    at Routes (http://localhost:5173/node_modules/.vite/deps/react-router-dom.js?v=1baeb357:4450:5)
    at Router (http://localhost:5173/node_modules/.vite/deps/react-router-dom.js?v=1baeb357:4393:15)
    at BrowserRouter (http://localhost:5173/node_modules/.vite/deps/react-router-dom.js?v=1baeb357:5141:5)
    at QueryClientProvider (http://localhost:5173/node_modules/.vite/deps/@tanstack_react-query.js?t=1722367666209&v=7740e8fa:2716:3)
    at MotionWrapper (http://localhost:5173/node_modules/.vite/deps/chunk-UYPYS5OR.js?v=3f512e7b:8195:5)
    at ProviderChildren (http://localhost:5173/node_modules/.vite/deps/chunk-UYPYS5OR.js?v=3f512e7b:8304:5)
    at ConfigProvider (http://localhost:5173/node_modules/.vite/deps/chunk-UYPYS5OR.js?v=3f512e7b:8582:27)
    at App
Consider adding an error boundary to your tree to customize error handling behavior.
Visit https://reactjs.org/link/error-boundaries to learn more about error boundaries.
logCapturedError @ chunk-KAPPEO6M.js?v=3f512e7b:14052
update.callback @ chunk-KAPPEO6M.js?v=3f512e7b:14072
callCallback @ chunk-KAPPEO6M.js?v=3f512e7b:11268
commitUpdateQueue @ chunk-KAPPEO6M.js?v=3f512e7b:11285
commitLayoutEffectOnFiber @ chunk-KAPPEO6M.js?v=3f512e7b:17115
commitLayoutMountEffects_complete @ chunk-KAPPEO6M.js?v=3f512e7b:18008
commitLayoutEffects_begin @ chunk-KAPPEO6M.js?v=3f512e7b:17997
commitLayoutEffects @ chunk-KAPPEO6M.js?v=3f512e7b:17948
commitRootImpl @ chunk-KAPPEO6M.js?v=3f512e7b:19381
commitRoot @ chunk-KAPPEO6M.js?v=3f512e7b:19305
finishConcurrentRender @ chunk-KAPPEO6M.js?v=3f512e7b:18788
performConcurrentWorkOnRoot @ chunk-KAPPEO6M.js?v=3f512e7b:18746
workLoop @ chunk-KAPPEO6M.js?v=3f512e7b:197
flushWork @ chunk-KAPPEO6M.js?v=3f512e7b:176
performWorkUntilDeadline @ chunk-KAPPEO6M.js?v=3f512e7b:384
Show 15 more frames
Show lessUnderstand this error
chunk-KAPPEO6M.js?v=3f512e7b:14052 The above error occurred in the <ArticleList> component:
    at ArticleList (http://localhost:5173/src/pages/articles/ArticleList.tsx:23:26)
    at RenderedRoute (http://localhost:5173/node_modules/.vite/deps/react-router-dom.js?v=1baeb357:4015:5)
    at Outlet (http://localhost:5173/node_modules/.vite/deps/react-router-dom.js?v=1baeb357:4386:26)
    at div
    at main
    at http://localhost:5173/node_modules/.vite/deps/chunk-UYPYS5OR.js?v=3f512e7b:64198:16
    at Content
    at div
    at http://localhost:5173/node_modules/.vite/deps/chunk-UYPYS5OR.js?v=3f512e7b:64217:16
    at Layout
    at div
    at http://localhost:5173/node_modules/.vite/deps/chunk-UYPYS5OR.js?v=3f512e7b:64217:16
    at Layout
    at ThemedLayoutContextProvider (http://localhost:5173/node_modules/.vite/deps/@refinedev_antd.js?v=37a19b68:45982:26)
    at ThemedLayoutV2 (http://localhost:5173/node_modules/.vite/deps/@refinedev_antd.js?v=37a19b68:46097:26)
    at RenderedRoute (http://localhost:5173/node_modules/.vite/deps/react-router-dom.js?v=1baeb357:4015:5)
    at Routes (http://localhost:5173/node_modules/.vite/deps/react-router-dom.js?v=1baeb357:4450:5)
    at Router (http://localhost:5173/node_modules/.vite/deps/react-router-dom.js?v=1baeb357:4393:15)
    at BrowserRouter (http://localhost:5173/node_modules/.vite/deps/react-router-dom.js?v=1baeb357:5141:5)
    at QueryClientProvider (http://localhost:5173/node_modules/.vite/deps/@tanstack_react-query.js?t=1722367666209&v=7740e8fa:2716:3)
    at MotionWrapper (http://localhost:5173/node_modules/.vite/deps/chunk-UYPYS5OR.js?v=3f512e7b:8195:5)
    at ProviderChildren (http://localhost:5173/node_modules/.vite/deps/chunk-UYPYS5OR.js?v=3f512e7b:8304:5)
    at ConfigProvider (http://localhost:5173/node_modules/.vite/deps/chunk-UYPYS5OR.js?v=3f512e7b:8582:27)
    at App
Consider adding an error boundary to your tree to customize error handling behavior.
Visit https://reactjs.org/link/error-boundaries to learn more about error boundaries.
logCapturedError @ chunk-KAPPEO6M.js?v=3f512e7b:14052
update.callback @ chunk-KAPPEO6M.js?v=3f512e7b:14072
callCallback @ chunk-KAPPEO6M.js?v=3f512e7b:11268
commitUpdateQueue @ chunk-KAPPEO6M.js?v=3f512e7b:11285
commitLayoutEffectOnFiber @ chunk-KAPPEO6M.js?v=3f512e7b:17115
commitLayoutMountEffects_complete @ chunk-KAPPEO6M.js?v=3f512e7b:18008
commitLayoutEffects_begin @ chunk-KAPPEO6M.js?v=3f512e7b:17997
commitLayoutEffects @ chunk-KAPPEO6M.js?v=3f512e7b:17948
commitRootImpl @ chunk-KAPPEO6M.js?v=3f512e7b:19381
commitRoot @ chunk-KAPPEO6M.js?v=3f512e7b:19305
finishConcurrentRender @ chunk-KAPPEO6M.js?v=3f512e7b:18788
performConcurrentWorkOnRoot @ chunk-KAPPEO6M.js?v=3f512e7b:18746
workLoop @ chunk-KAPPEO6M.js?v=3f512e7b:197
flushWork @ chunk-KAPPEO6M.js?v=3f512e7b:176
performWorkUntilDeadline @ chunk-KAPPEO6M.js?v=3f512e7b:384
Show 15 more frames
Show lessUnderstand this error
chunk-KAPPEO6M.js?v=3f512e7b:19441 Uncaught Error: No QueryClient set, use QueryClientProvider to set one
    at useQueryClient (chunk-TV2X25GZ.js?v=3f512e7b:6125:11)
    at useInvalidateAuthStore (chunk-TV2X25GZ.js?v=3f512e7b:8917:11)
    at useLogout (chunk-TV2X25GZ.js?v=3f512e7b:8923:11)
    at ThemedSiderV2 (@refinedev_antd.js?v=37a19b68:46067:553)
    at renderWithHooks (chunk-KAPPEO6M.js?v=3f512e7b:11568:26)
    at mountIndeterminateComponent (chunk-KAPPEO6M.js?v=3f512e7b:14946:21)
    at beginWork (chunk-KAPPEO6M.js?v=3f512e7b:15934:22)
    at beginWork$1 (chunk-KAPPEO6M.js?v=3f512e7b:19781:22)
    at performUnitOfWork (chunk-KAPPEO6M.js?v=3f512e7b:19226:20)
    at workLoopSync (chunk-KAPPEO6M.js?v=3f512e7b:19165:13)cls
npm install @tanstack/react-query
npm run dev
npm uninstall react-query
npm uninstall react-query
npm run dev
npm install @tanstack/react-query
npm uninstall @tanstack/react-query
npm run dev
npm uninstall @tanstack/react-query
npm install @tanstack/react-query
npm run dev
rm -rf node_modules
npm install
npm run dev
npm install
npm run dev
rm -rf node_modules
rm -rf node_modules
rm -rf node_modules
rm package-lock.json
npm install
npm run dev
npm run dev
npm run dev
npm run refine devtools init
npm run dev
npm run dev
npm run dev
npm run dev
uvicorn main:app --reload
(base) root@e8e3b9aba431:~# uvicorn main:app --reload
cd backend/
uvicorn main:app --reload
cd ..
backend (base) root@e8e3b9aba431:~/backend# ^C
uvicorn main:backend --reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000
cd backend/
uvicorn main:app --reload --host 0.0.0.0 --port 8000
cd ..
cd app/
uvicorn main:app --reload --host 0.0.0.0 --port 8000
(base) root@e8e3b9aba431:~/app# ^C
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
cd ..
(base) root@e8e3b9aba431:~/app# ^C
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
pip install jose
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
pip unistall jose
pip uninstall jose
pip install -r requirements.txt 
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
(base) root@e8e3b9aba431:~# ^C
alembic init alembic
alembic init alembic
alembic revision --autogenerate -m "Initial migration"
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
pip install pydantic-settings
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
clear
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
npm install @remix-run/node @remix-run/react @refinedev/core @refinedev/antd @refinedev/devtools @refinedev/kbar antd axios react-router-dom
npm run dev
pip install passlib
npm install @remix-run/node @remix-run/react
npm install dotenv
,npm i @refinedev/react-router-v6 react-router-dom
npm i @refinedev/react-router-v6 react-router-dom
npm install @tanstack/react-query
Show 8 more frames
npm install @tanstack/react-query
npm install @tanstack/react-query
npm uninstall @tanstack/react-query
npm uninstall @refinedev/gatsby
npm run refine devtools init
npm run refine devtools initnpm install @tanstack/react-query
npm install @tanstack/react-query
