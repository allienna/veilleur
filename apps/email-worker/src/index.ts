export default {
  async email(
    message: ForwardableEmailMessage,
    _env: Record<string, unknown>,
    _ctx: ExecutionContext,
  ): Promise<void> {
    // Placeholder — will be implemented in F-008
    console.log(`Received email from ${message.from} to ${message.to}`);
  },
};
