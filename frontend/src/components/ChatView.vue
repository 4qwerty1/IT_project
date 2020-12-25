<template>
  <div>
    <md-content>
      <div class="left">
        <md-avatar>
          <img src="../assets/avatars/hedgehog_512.jpg" alt="Avatar">
        </md-avatar>
        <span class="name">hedgehog319</span>
      </div>
    </md-content>
  </div>
</template>

<script>
export default {
  name: "ChatView"
}
</script>

<style lang="scss" scoped>

.name {
  position: absolute;
  padding-left: 10px;
}

.left {
  position: relative;
  display: inline-block;
  margin-right: 90%;
  margin-top: 1%;
  //float: left;
}

</style>