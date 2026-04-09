export default {
  async email(
    _message: ForwardableEmailMessage,
    _env: Record<string, unknown>,
    _ctx: ExecutionContext,
  ): Promise<void> {
    // Placeholder — will be implemented in F-008
    console.log("Received email");
  },
};
