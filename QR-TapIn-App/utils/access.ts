import axios from "axios";

const url = "https://n7dwb6cv-80.asse.devtunnels.ms/api";

const endpoint_middleware = (endpoint: string) => {
  if (!endpoint.startsWith("/")) {
    endpoint = `/${endpoint}`;
  }
  if (!endpoint.endsWith("/")) {
    endpoint = `${endpoint}/`;
  }
  return endpoint;
};

export async function get_unauth(endpoint: string, params?: unknown) {
  const { data } = await axios.get(
    `${url}${endpoint_middleware(endpoint)}`,
    params || {},
  );
  return data;
}

export async function post_unauth(endpoint: string, params?: unknown) {
  const { data } = await axios.post(
    `${url}${endpoint_middleware(endpoint)}`,
    params || {},
  );
  return data;
}

export async function get(endpoint: string, params?: unknown) {
  const { data } = await axios.get(`${url}${endpoint_middleware(endpoint)}`, {
    params: params || {},
    headers: {},
  });
  return data;
}

export async function post(endpoint: string, params?: unknown) {
  const { data } = await axios.post(
    `${url}${endpoint_middleware(endpoint)}`,
    params || {},
    {
      headers: {},
    },
  );
  return data;
}
