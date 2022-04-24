<script lang="tsx">
  import { defineComponent, renderList } from "vue"

  export default defineComponent({
    name: "petequ",
    setup(props, { emit, slots }) {
      return () => (
        <div class="flex flex-wrap equ-profile">
          <div class="equ-profile-item">
            <div class="row-name">红色</div>
            <calc-select class="!h-20px flex-1"></calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">绿色</div>
            <calc-select class="!h-20px flex-1"></calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">蓝色</div>
            <calc-select class="!h-20px flex-1"></calc-select>
          </div>
        </div>
      )
    }
  })
</script>
