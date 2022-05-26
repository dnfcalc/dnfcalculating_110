import { is_folder_url, headers } from "./utils"
import fetch from "node-fetch"

const _host = "https://wwn.lanzout.com/"

export interface file {
  duan: string
  id: string
  name_all: string
  size: string
  time: string
}

export async function get_folder_info_by_url(share_url: string, dir_pwd: string = "") {
  let html = await is_folder_url(share_url)
  if (html == "") return undefined
  const folder_id = new RegExp("'fid':'?(d+)'?,").exec(html)?.[0]
  const lx = new RegExp("'lx':'?(\\d)'?,").exec(html)?.[0]
  const k = new RegExp("var [0-9a-z]{6} = '([0-9a-z]{15,})';").exec(html)?.[0]
  const t = new RegExp("var [0-9a-z]{6} = '(\\d{10})';").exec(html)?.[0]

  fetch(_host + "/filemoreajax.php", {
    headers: headers,
    method: "POST",
    body: JSON.stringify({
      lx: lx,
      pg: 1,
      k: k,
      t: t,
      fid: folder_id,
      pwd: dir_pwd
    })
  }).then(res => {
    return res.json()
  })
}
